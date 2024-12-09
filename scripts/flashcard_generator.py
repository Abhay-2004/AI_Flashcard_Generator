# flashcard_generator.py

import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Configure the genai library with your API key
genai.configure(api_key=GEMINI_API_KEY)

# Instantiate the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash-latest")

def summarize_text(text):
    """
    Generates a summary of the provided text using the Gemini API.
    
    Args:
        text (str): The input text to summarize.
    
    Returns:
        str or None: The generated summary or None if an error occurs.
    """
    summary_prompt = (
        "Provide a concise and clear summary of the following text without adding any extra information:\n\n"
        f"{text}"
    )
    try:
        response = model.generate_content(summary_prompt)
        summary = response.text.strip()
        return summary
    except Exception as e:
        print(f"Error during summarization: {e}")
        return None

def generate_flashcards(summary, num_flashcards=5):
    """
    Generates flashcards based on the provided summary using the Gemini API.
    
    Args:
        summary (str): The summary text to base flashcards on.
        num_flashcards (int): Number of flashcards to generate.
    
    Returns:
        str or None: The generated flashcards or None if an error occurs.
    """
    flashcards_prompt = (
        f"Based on the summary below, generate exactly {num_flashcards} question-answer flashcards.\n\n"
        "Format each flashcard as follows without numbering:\n"
        "Q: [Your question here]\n"
        "A: [Your answer here]\n\n"
        f"Summary:\n{summary}"
    )
    try:
        response = model.generate_content(flashcards_prompt)
        flashcards = response.text.strip()
        return flashcards
    except Exception as e:
        print(f"Error during flashcard generation: {e}")
        return None

def create_flashcards_from_text(input_text, num_flashcards=5):
    """
    Creates a summary and flashcards from the input text.
    
    Args:
        input_text (str): The course material text.
        num_flashcards (int): Number of flashcards to generate.
    
    Returns:
        tuple: A tuple containing the summary and flashcards.
    """
    print("Generating summary...")
    summary = summarize_text(input_text)
    if not summary:
        return "Summarization failed.", ""
    
    print("Generating flashcards...")
    flashcards = generate_flashcards(summary, num_flashcards)
    if not flashcards:
        return summary, "Flashcard generation failed."
    
    return summary, flashcards