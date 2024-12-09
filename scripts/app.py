# app.py

import streamlit as st
from flashcard_generator import create_flashcards_from_text
import pandas as pd
from fpdf import FPDF
import io
import os
import re

def generate_pdf(flashcards):
    """
    Converts flashcards text into a PDF file using fpdf2 with Unicode support.
    
    Args:
        flashcards (str): The flashcards text.
    
    Returns:
        BytesIO: A buffer containing the PDF data.
    """
    pdf = FPDF()
    pdf.add_page()
    
    # Get the absolute path to the font file
    script_dir = os.path.dirname(__file__)  # Directory of app.py
    font_path = os.path.join(script_dir, "fonts", "DejaVuSans.ttf")
    
    # Check if the font file exists
    if not os.path.exists(font_path):
        st.error(f"Font file not found at {font_path}. Please ensure the font file is in the 'fonts' directory.")
        return None
    
    # Add the DejaVu font with Unicode support
    pdf.add_font("DejaVu", "", font_path, uni=True)
    pdf.set_font("DejaVu", size=12)
    
    # Split flashcards into individual Q&A pairs
    # Assuming each flashcard has Q: ... and A: ... without numbering
    flashcard_entries = re.split(r'\n\s*\n', flashcards)  # Split by empty lines
    
    for idx, entry in enumerate(flashcard_entries, 1):
        if entry.strip():
            # Extract Q and A using regex
            match = re.match(r'Q:\s*(.*?)\s*A:\s*(.*)', entry, re.DOTALL)
            if match:
                question = match.group(1).strip()
                answer = match.group(2).strip()
                pdf.multi_cell(0, 10, f"Flashcard {idx}:\nQ: {question}\nA: {answer}\n")
                pdf.ln(5)
            else:
                # Handle unexpected formatting
                pdf.multi_cell(0, 10, f"Flashcard {idx}:\n{entry}\n")
                pdf.ln(5)
    
    # Save PDF to a bytes buffer
    buffer = io.BytesIO()
    pdf.output(buffer)
    buffer.seek(0)
    return buffer

def parse_flashcards(flashcards):
    """
    Parses the flashcards text and returns a list of dictionaries with questions and answers.
    
    Args:
        flashcards (str): The flashcards text.
    
    Returns:
        list: A list of dictionaries containing 'Question' and 'Answer' keys.
    """
    flashcard_entries = re.split(r'\n\s*\n', flashcards)  # Split by empty lines
    parsed_flashcards = []
    
    for entry in flashcard_entries:
        if entry.strip():
            # Extract Q and A using regex
            match = re.match(r'Q:\s*(.*?)\s*A:\s*(.*)', entry, re.DOTALL)
            if match:
                question = match.group(1).strip()
                answer = match.group(2).strip()
                parsed_flashcards.append({'Question': question, 'Answer': answer})
            else:
                # Handle unexpected formatting
                parsed_flashcards.append({'Question': 'N/A', 'Answer': entry.strip()})
    
    return parsed_flashcards

def main():
    # Set Streamlit page configuration
    st.set_page_config(page_title="AI-Powered Flashcard Generator", layout="wide")
    
    # Optional: Add a logo or image
    # st.image("path/to/logo.png", width=150)
    
    st.title("AI-Powered Flashcard Generator")
    st.write("Enter your course material below, and the AI will generate flashcards for you.")
    
    # Sidebar for additional controls
    st.sidebar.header("Settings")
    
    num_flashcards = st.sidebar.slider("Number of Flashcards", min_value=3, max_value=10, value=5)
    
    # File uploader
    uploaded_file = st.sidebar.file_uploader("Upload Course Material (TXT)", type=["txt"])
    
    if uploaded_file is not None:
        try:
            input_text = uploaded_file.read().decode('utf-8')
            st.text_area("Course Material", value=input_text, height=300)
        except UnicodeDecodeError:
            st.error("Error decoding the uploaded file. Please ensure it's a UTF-8 encoded TXT file.")
            input_text = ""
    else:
        input_text = st.text_area("Course Material", height=300)
    
    if st.button("Generate Flashcards"):
        if input_text.strip():
            with st.spinner("Generating summary and flashcards..."):
                summary, flashcards = create_flashcards_from_text(input_text, num_flashcards)
            
            # Display Summary
            if summary != "Summarization failed.":
                st.subheader("Summary")
                st.write(summary)
            else:
                st.error(summary)
            
            # Display Flashcards
            if flashcards and flashcards != "Flashcard generation failed.":
                st.subheader("Flashcards")
                
                # Parse flashcards
                parsed_flashcards = parse_flashcards(flashcards)
                
                if len(parsed_flashcards) != num_flashcards:
                    st.warning(
                        f"The AI generated {len(parsed_flashcards)} flashcards instead of the requested {num_flashcards}."
                    )
                
                for idx, card in enumerate(parsed_flashcards, 1):
                    st.markdown(f"**Flashcard {idx}:**")
                    st.write(f"**Q:** {card['Question']}")
                    st.write(f"**A:** {card['Answer']}")
                    st.markdown("---")
                
                # Convert flashcards to CSV
                df = pd.DataFrame(parsed_flashcards)
                csv = df.to_csv(index=False)
                
                # Provide download options
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.download_button(
                        label="Download Flashcards as TXT",
                        data=flashcards,
                        file_name="flashcards.txt",
                        mime="text/plain"
                    )
                
                with col2:
                    st.download_button(
                        label="Download Flashcards as CSV",
                        data=csv,
                        file_name="flashcards.csv",
                        mime="text/csv"
                    )
                
                with col3:
                    pdf_buffer = generate_pdf(flashcards)
                    if pdf_buffer:
                        st.download_button(
                            label="Download Flashcards as PDF",
                            data=pdf_buffer,
                            file_name="flashcards.pdf",
                            mime="application/pdf"
                        )
            elif flashcards == "Flashcard generation failed.":
                st.error(flashcards)
        else:
            st.warning("Please enter some text or upload a file to generate flashcards.")

if __name__ == "__main__":
    main()