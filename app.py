import streamlit as st
import tempfile
from helper import process_files, generate_topic_from_filename, get_ai_model
import re

def strip_duplicate_titles(content, main_title, topic_name):
    """Remove duplicate main title and topic name from the beginning of content."""
    # Remove all leading whitespace and newlines
    content = content.lstrip()
    
    # Remove main title (# main_title) if present at the start
    main_title_pattern = r'^#{1,3}\s*' + re.escape(main_title) + r'\s*\n+'
    content = re.sub(main_title_pattern, '', content)
    
    # Remove topic name (## topic_name) if present at the start
    topic_pattern = r'^#{1,3}\s*' + re.escape(topic_name) + r'\s*\n+'
    content = re.sub(topic_pattern, '', content)
    
    # Clean up any remaining leading whitespace
    content = content.lstrip()
    
    return content

# Page configuration
st.set_page_config(
    page_title="DevNotes-AI",
    page_icon="📚",
    layout="wide"
)

# Title
st.title("📚 DevNotes-AI")
st.markdown("**Transform your code files into study notes with AI!**")

# Initialize session state
if 'processed_files' not in st.session_state:
    st.session_state.processed_files = []
if 'current_file_index' not in st.session_state:
    st.session_state.current_file_index = 0
if 'editing_mode' not in st.session_state:
    st.session_state.editing_mode = False
if 'uploaded_files' not in st.session_state:
    st.session_state.uploaded_files = []
if 'file_details' not in st.session_state:
    st.session_state.file_details = {}
if 'files_processed' not in st.session_state:
    st.session_state.files_processed = False
if 'final_notes' not in st.session_state:
    st.session_state.final_notes = ""

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    
    # AI Provider Selection
    st.subheader("🤖 AI Provider")
    ai_provider = st.selectbox(
        "Choose AI Provider:",
        ["Gemini", "OpenAI", "Claude"],
        help="Select which AI service to use"
    )
    
    # Model Selection based on provider
    st.subheader("🤖 AI Model")
    if ai_provider == "Gemini":
        models = [
            "gemini-2.5-pro",
            "gemini-2.5-flash",
        ]
        default_model = "gemini-2.5-flash"
    elif ai_provider == "OpenAI":
        models = [
            "gpt-5-2025-08-07"
            "gpt-4o",
            "gpt-4o-mini",
            "gpt-4-turbo",
        ]
        default_model = "gpt-4o"
    else:  # Claude
        models = [
            "claude-haiku-4-5-20251001",
            "claude-sonnet-4-5-20250929",
            "claude-opus-4-1-20250805"
        ]
        default_model = "claude-sonnet-4-5-20250929"
    
    model_name = st.selectbox(
        "Choose Model:",
        models,
        index=models.index(default_model) if default_model in models else 0,
        help="Select the specific model to use"
    )
    
    # API Key Input
    api_key = st.text_input(
        f"{ai_provider} API Key:",
        type="password",
        help=f"Enter your {ai_provider} API key"
    )
    
    # Privacy notice
    st.info("🔒 **Privacy Note:** Your API key is used only for API calls and is never stored on the site.")
    
    # Main title
    st.subheader("📝 Notes Settings")
    main_title = st.text_input(
        "Notes Title",
        value="My Study Notes",
        help="Title for your generated notes"
    )
    
    # File Upload Section
    st.subheader("📁 Upload Files")
    uploaded_files = st.file_uploader(
        "Choose code files",
        type=['py', 'js', 'ipynb', 'java', 'cpp', 'c', 'txt'],
        accept_multiple_files=True,
        help="Upload your code files from anywhere on your PC"
    )

# Main content
if uploaded_files:
    st.success(f"✅ {len(uploaded_files)} files uploaded!")
    
    # Save uploaded files and update session state
    temp_files = []
    for uploaded_file in uploaded_files:
        # Create temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp_file:
            tmp_file.write(uploaded_file.getbuffer())
            temp_files.append(tmp_file.name)
            
            # Initialize file details
            if tmp_file.name not in st.session_state.file_details:
                st.session_state.file_details[tmp_file.name] = {
                    'topic': generate_topic_from_filename(uploaded_file.name),
                    'suggestion': "Explain clearly and simply"
                }
    
    st.session_state.uploaded_files = temp_files
    
    # Show uploaded files with concise configuration
    st.subheader("📝 Configure Your Files")
    st.info("💡 **Tip:** You can edit the topic names and suggestions below. These will be used as section titles in your final notes.")
    
    # Create a more concise table-like view
    for i, file_path in enumerate(st.session_state.uploaded_files):
        original_name = uploaded_files[i].name
        
        st.write(f"### 📄 {original_name}")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.write("**Section Topic:**")
            topic = st.text_input(
                "Section Topic:",
                value=st.session_state.file_details[file_path]['topic'],
                key=f"topic_{i}",
                help="This will be the section title in your notes",
                label_visibility="collapsed"
            )
            st.session_state.file_details[file_path]['topic'] = topic
        
        with col2:
            st.write("**Any Suggestions:**")
            suggestion = st.text_input(
                "Any Suggestions:",
                value=st.session_state.file_details[file_path]['suggestion'],
                key=f"suggestion_{i}",
                help="How should the AI explain this file",
                label_visibility="collapsed"
            )
            st.session_state.file_details[file_path]['suggestion'] = suggestion
        
        st.markdown("---")
    
    # Generate button
    if st.button("🚀 Start Processing", type="primary", use_container_width=True):
        if not main_title.strip():
            st.error("Please enter a title for your notes!")
        elif not api_key.strip():
            st.error("Please enter your API key!")
        else:
            try:
                # Get AI model
                ai_model = get_ai_model(ai_provider, model_name, api_key)
                
                # Prepare data for processing
                topics = [st.session_state.file_details[file_path]['topic'] for file_path in st.session_state.uploaded_files]
                suggestions = [st.session_state.file_details[file_path]['suggestion'] for file_path in st.session_state.uploaded_files]
                
                # Process files with progress updates
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                def update_progress(current, total, message):
                    progress = current / total
                    progress_bar.progress(progress)
                    status_text.text(f"{message} ({current}/{total})")
                
                with st.spinner("Processing files... Please wait."):
                    st.session_state.processed_files, previous_topics = process_files(
                        st.session_state.uploaded_files, 
                        main_title, 
                        topics,
                        suggestions,
                        progress_callback=update_progress,
                        ai_model=ai_model
                    )
                    st.session_state.editing_mode = True
                    st.session_state.current_file_index = 0
                    st.session_state.files_processed = True
                    st.rerun()
                    
            except Exception as e:
                st.error(f"❌ Error: {e}")
                st.info("Please check your API key and try again.")

else:
    st.info("👆 Please upload your code files using the sidebar to get started!")

# Editing mode - show generated markdown for each file
if st.session_state.editing_mode and st.session_state.processed_files:
    current_file = st.session_state.processed_files[st.session_state.current_file_index]
    
    st.markdown("---")
    st.subheader(f"📝 Editing: {current_file['file_path']}")
    st.write(f"**Topic:** {current_file['topic_name']}")
    
    # Show progress
    progress = (st.session_state.current_file_index + 1) / len(st.session_state.processed_files)
    st.progress(progress)
    st.write(f"File {st.session_state.current_file_index + 1} of {len(st.session_state.processed_files)}")
    
    # Editable markdown
    edited_notes = st.text_area(
        "Generated Notes (Edit if needed):",
        value=current_file['notes'],
        height=400,
        key=f"edit_{st.session_state.current_file_index}"
    )
    
    # Update the notes in session state
    st.session_state.processed_files[st.session_state.current_file_index]['notes'] = edited_notes
    
    col1, col2, col3 = st.columns([1, 1, 2])
    
    with col1:
        if st.session_state.current_file_index > 0:
            if st.button("⬅️ Previous"):
                st.session_state.current_file_index -= 1
                st.rerun()
    
    with col2:
        if st.session_state.current_file_index < len(st.session_state.processed_files) - 1:
            if st.button("Next ➡️"):
                st.session_state.current_file_index += 1
                st.rerun()
        else:
            if st.button("✅ Finish & Generate"):
                # Combine all notes with proper formatting
                combined_notes = f"# {main_title}\n\n"
                
                for file_data in st.session_state.processed_files:
                    # Add section heading
                    combined_notes += f"## {file_data['topic_name']}\n\n"
                    
                    # Get the notes content and remove any duplicate titles
                    notes_content = file_data['notes']
                    
                    # Strip duplicate titles using the helper function
                    notes_content = strip_duplicate_titles(notes_content, main_title, file_data['topic_name'])
                    
                    # Add the cleaned notes content
                    combined_notes += notes_content + "\n\n"
                
                # Save to session state
                st.session_state.final_notes = combined_notes
                
                # Save markdown file
                markdown_filename = f"{main_title.replace(' ', '_').lower()}_notes.md"
                with open(markdown_filename, 'w', encoding='utf-8') as f:
                    f.write(combined_notes)
                
                st.success("✅ Notes generated successfully!")
                st.rerun()

# Show final preview and download
if st.session_state.final_notes:
    st.markdown("---")
    st.subheader("📖 Final Notes Preview")
    
    # Create tabs for better organization
    tab1, tab2 = st.tabs(["📖 Preview", "📥 Download"])
    
    with tab1:
        # Nice preview with proper markdown rendering
        st.markdown(st.session_state.final_notes)
    
    with tab2:
        st.subheader("📥 Download Your Notes")
        
        # Download button
        markdown_filename = f"{main_title.replace(' ', '_').lower()}_notes.md"
        st.download_button(
            label="📝 Download Markdown File",
            data=st.session_state.final_notes,
            file_name=markdown_filename,
            mime="text/markdown",
            use_container_width=True
        )
        
        # Show file info
        st.info(f"📄 **File:** {markdown_filename}")
        st.info(f"📊 **Size:** {len(st.session_state.final_notes)} characters")
        
        # MD to PDF conversion info
        st.markdown("---")
        st.subheader("📄 Convert to PDF")
        st.write("Want to convert your Markdown file to PDF? Use these online tools:")
        st.markdown("""
        - **[Markdown to PDF](https://www.markdowntopdf.com/)** - Simple and fast conversion
        - **[Dillinger](https://dillinger.io/)** - Markdown editor with PDF export
        """)
        
        # Reset button
        if st.button("🔄 Start New Project", type="secondary"):
            # Reset all session state
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

# Footer
st.markdown("---")
st.markdown("*DevNotes-AI - Simple code to notes conversion*")