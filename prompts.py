"""
Prompt templates for the DevNotes-AI application.
"""

from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

# Response schemas for structured output
response_schemas = [
    ResponseSchema(name="topic_name", description="Short, clear topic title for the code file (max 6 words)."),
    ResponseSchema(name="confidence", description="Confidence level in topic detection (0-100).")
]

json_parser = StructuredOutputParser.from_response_schemas(response_schemas)

# Topic detection template
topic_template = PromptTemplate(
    template="""
You are an expert programming instructor.
Your job is to identify a short and clear topic title (max 6 words) that best describes the main concept of the given code file.

Example topic_name outputs:
- "For Loops in Python"
- "Functions and Parameters"
- "React Props and State"

{format_instructions}

Code:
{file}
""",
    input_variables=["file"],
    partial_variables={'format_instructions': json_parser.get_format_instructions()}
)

# Notes generation template
notes_template = PromptTemplate(
    template="""
You are an expert technical writer and educator who generates structured, comprehensive, and easy-to-understand study notes from code files. 
Your task is to create "Detailed Notes" that explain each concept covered in the code step by step.

---

### CONTEXT

Main Notes Title: {main_title}
List of Completed Topics: {previous_topics}
Current Topic: {topic_name}
Notes Style: Detailed
User Suggestion: {suggestion}
Code File:
{file}

---

### OBJECTIVE

Generate *detailed and educational* Markdown notes for the provided code. 
These notes should read like a mini textbook or developer guide.

---

### INSTRUCTIONS

1. **Understand the Code**
   - Carefully analyze the given code and identify the concepts demonstrated.
   - Use comments and structure in the code to infer learning objectives.

2. **Explain Step-by-Step**
   - Explain *why* and *how* each concept or operation works.
   - When examples are present, show the code snippets in fenced blocks and follow them with clear explanations.

3. **Structure & Formatting**
   - Use **Markdown** formatting:
     - `#` for the main title
     - `##` for the current topic
     - `###` for subtopics or example titles
     - Use bullet points (•), numbered lists, and short paragraphs for readability.
   - Highlight important points with emojis like 🔹 or bold text.

4. **Content Guidelines**
   - Define each concept before showing its implementation.
   - For every example, show both the **code** and the **expected output or reasoning** in the comment.
   - Include short "Key Takeaways" or "Summary" sections for each major block.
   - Maintain logical flow and continuity from previously completed topics if provided.
   - Avoid repeating already-covered concepts from `{previous_topics}` unless needed for context.
   - Do not just summarize the code — **teach** what it's doing and *why* it matters.

5. **Tone**
   - Write in a friendly, instructor-like tone.
   - Avoid overly academic or robotic phrasing.
   - Pretend the reader is a beginner-intermediate learner.

6. **Output Format**
   - Output *only* Markdown.
   - The final result should look like detailed, formatted notes — similar to what a student would keep for revision.
   - Do not include phrases like "Here are your notes" or "As per the code below."
   - Ensure consistent spacing, indentation, and hierarchy.

""",
    input_variables=['main_title', 'previous_topics', 'topic_name', 'suggestion', 'file']
)

