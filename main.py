from helper import file_reader, process_files, format_final_notes, markdown_to_pdf

def main():
    """Main function to generate notes from code files."""
    print("📚 DevNotes-AI: Code to Study Notes Generator")
    print("=" * 50)
    
    # Get user input for main title
    main_title = input("Enter the main title for your notes (e.g., 'Complete Python Notes'): ").strip()
    if not main_title:
        main_title = "Complete Study Notes"
    
    # Get file list from user
    print("\nEnter file paths (one per line, press Enter twice when done):")
    file_list = []
    while True:
        file_path = input("File path: ").strip()
        if not file_path:
            break
        file_list.append(file_path)
    
    if not file_list:
        print("❌ No files provided. Exiting.")
        return
    
    print(f"\n📁 Processing {len(file_list)} files...")
    
    try:
        # Process files and generate notes
        all_notes, previous_topics = process_files(file_list, main_title)
        
        # Combine all notes
        combined_notes = f"# {main_title}\n\n" + "\n\n".join(all_notes)
        
        # Optional: Format final notes
        print("\n🔧 Formatting notes...")
        formatted_notes = format_final_notes(combined_notes)

        markdown_filename = f"{main_title.replace(' ', '_').lower()}_notes.md"

        # Convert to PDF
        pdf_filename = f"{main_title.replace(' ', '_').lower()}_notes.pdf"
        print(f"\n📄 Converting to PDF...")
        success = markdown_to_pdf(formatted_notes, pdf_filename)
        
        if success:
            print(f"\n🎉 Success! Generated:")
            print(f"   📝 Markdown: {markdown_filename}")
            print(f"   📄 PDF: {pdf_filename}")
        else:
            print(f"\n⚠️  Markdown saved but PDF conversion failed.")
            print(f"   📝 Markdown: {markdown_filename}")
        
    except Exception as e:
        print(f"❌ Error processing files: {e}")
        print("Make sure all required dependencies are installed:")
        print("pip install langchain-google-genai python-dotenv langchain markdown2 pdfkit")

if __name__ == "__main__":
    main()