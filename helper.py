import json
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
import os
from langchain_core.output_parsers import StrOutputParser
import markdown2
import re
from prompts import notes_template

def get_ai_model(provider, model_name, api_key):
    """Get AI model based on provider, model name, and API key."""
    if provider == "Gemini":
        return ChatGoogleGenerativeAI(model=model_name, google_api_key=api_key)
    elif provider == "OpenAI":
        return ChatOpenAI(model=model_name, openai_api_key=api_key)
    elif provider == "Claude":
        return ChatAnthropic(model=model_name, anthropic_api_key=api_key)
    else:
        raise ValueError(f"Unsupported provider: {provider}")

parser = StrOutputParser()

def generate_detailed_notes(main_title, previous_topics, topic_name, suggestion, file_content, ai_model):
    """Generate detailed notes for a given file content."""
    current_chain = notes_template | ai_model | parser
    
    result = current_chain.invoke({
        "main_title": main_title,
        "previous_topics": previous_topics,
        "topic_name": topic_name,
        "suggestion": suggestion,
        "file": file_content
    })
    return result

def process_files(file_list, main_title="Complete Study Notes", topics=None, suggestions=None, progress_callback=None, ai_model=None):
    """
    Process a list of files and generate detailed notes for each.
    Returns individual notes for editing.
    
    Args:
        file_list: List of file paths to process
        main_title: Main title for the notes
        topics: Optional list of topic names (if None, will use file names)
        suggestions: Optional list of suggestions for each file
        progress_callback: Optional callback function for progress updates
        ai_model: AI model to use for processing (required)
    """
    if ai_model is None:
        raise ValueError("ai_model is required. Please provide an AI model instance.")
    
    all_notes = []
    previous_topics = ""
    
    # Use provided model
    current_model = ai_model
    
    # Default values if not provided
    if topics is None:
        topics = []
    if suggestions is None:
        suggestions = []
    
    for i, file_path in enumerate(file_list):
        print(f"📁 Processing file {i+1}/{len(file_list)}: {file_path}")
        
        # Update progress if callback provided
        if progress_callback:
            progress_callback(i, len(file_list), f"Processing {file_path}")
        
        content = file_reader(file_path)
        
        # Step 1 — Get topic name
        if i < len(topics) and topics[i] and topics[i].strip():
            # Use provided topic
            topic_name = topics[i].strip()
        else:
            # Use file name as topic (simple and fast)
            topic_name = generate_topic_from_filename(file_path)
        
        print(f"📝 Topic: {topic_name}")
        
        # Step 2 — Generate detailed notes
        suggestion = suggestions[i] if i < len(suggestions) else "Explain clearly and simply"
        
        notes = generate_detailed_notes(
            main_title=main_title,
            previous_topics=previous_topics,
            topic_name=topic_name,
            suggestion=suggestion,
            file_content=content,
            ai_model=current_model
        )
        
        all_notes.append({
            'file_path': file_path,
            'topic_name': topic_name,
            'notes': notes
        })
        
        # Step 3 — Update previous topics
        if previous_topics:
            previous_topics += f", {topic_name}"
        else:
            previous_topics = topic_name
    
    # Final progress update
    if progress_callback:
        progress_callback(len(file_list), len(file_list), "Processing complete!")
    
    return all_notes, previous_topics

def generate_topic_from_filename(file_path):
    """Generate a topic name from filename (fast alternative to AI detection)."""
    filename = os.path.basename(file_path)
    name_without_ext = os.path.splitext(filename)[0]
    
    # Clean up the filename
    topic = name_without_ext.replace('_', ' ').replace('-', ' ')
    
    # Capitalize words
    topic = ' '.join(word.capitalize() for word in topic.split())
    
    # Handle common patterns
    if 'numpy' in topic.lower():
        topic = topic.replace('Numpy', 'NumPy')
    if 'ipynb' in filename.lower():
        topic = topic.replace('.ipynb', '')
    
    return topic

def file_reader(file_path):
    """Read file content, handling both regular files and Jupyter notebooks."""
    for_extension = file_path.split(".")
    extension = for_extension[len(for_extension)-1]

    if extension == "ipynb":
        with open(file_path, "r", encoding="utf-8") as f:
            notebook = json.load(f)

        # Extract all code cells
        code_cells = [
            "".join(cell["source"])
            for cell in notebook.get("cells", [])
            if cell.get("cell_type") == "code"
        ]

        code_text = "\n".join(code_cells)
        return code_text

    else:
        with open(file_path, "r", encoding="utf-8") as f:
            code_text = f.read()
        return code_text