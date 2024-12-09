# AI-Powered Flashcard Generator

An interactive tool that uses AI to automatically generate flashcards from educational content. Built for students, teachers, and professionals who want to create effective study materials quickly and efficiently using the Gemini API.

## 🌟 Features

- **Smart Text Summarization**: Automatically condenses lengthy educational material into concise summaries
- **AI-Powered Flashcard Creation**: Generates relevant question-answer pairs from the summarized content
- **Multiple Export Formats**: Download your flashcards as TXT, CSV, or PDF files
- **User-Friendly Interface**: Built with Streamlit for an intuitive experience
- **File Upload Support**: Import content directly from text files
- **Customizable**: Choose how many flashcards to generate (3-10)

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- A Gemini API key from Google
- Git (for cloning the repository)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/AI-Powered-Flashcard-Generator.git
cd AI-Powered-Flashcard-Generator
```

2. Create and activate a virtual environment:
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Set up your Gemini API key:
- Create a `.env` file in the project root
- Add your API key:
```
GEMINI_API_KEY=your_api_key_here
```

### Running the Application

1. Ensure your virtual environment is activated
2. Launch the application:
```bash
streamlit run scripts/app.py
```
3. Open your web browser and navigate to `http://localhost:8501`

## 💡 How to Use

### Input Methods

1. **Direct Text Entry**:
   - Type or paste your study material into the text area
   - Ideal for quick content processing

2. **File Upload**:
   - Upload a `.txt` file containing your study material
   - Perfect for longer documents

### Generating Flashcards

1. Enter your study material using either input method
2. Use the sidebar slider to select the number of flashcards (3-10)
3. Click "Generate Flashcards"
4. Review the generated summary and flashcards
5. Download your flashcards in your preferred format (TXT, CSV, or PDF)

## 📁 Project Structure

```
AI-Powered-Flashcard-Generator/
├── fonts/
│   └── DejaVuSans.ttf        # Font for PDF export
├── scripts/
│   ├── app.py                # Main Streamlit application
│   └── flashcard_generator.py # AI logic for generating content
├── .env                      # API key configuration
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## 🛠️ Technical Details

### Core Components

- **Frontend**: Streamlit
- **AI Engine**: Google's Gemini API
- **PDF Generation**: FPDF2 library
- **Data Processing**: Pandas for CSV handling

### Key Functions

- `create_flashcards_from_text()`: Manages the overall flashcard generation process
- `summarize_text()`: Creates concise summaries using AI
- `generate_flashcards()`: Produces question-answer pairs
- `generate_pdf()`: Creates formatted PDF output

## 📝 Requirements

```
streamlit>=1.10.0
google-generativeai>=0.3.0
python-dotenv>=0.19.0
pandas>=1.3.0
fpdf2>=2.4.0
```

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## 👥 Support

If you encounter any issues or have questions:

- Open an issue on GitHub
- Email: your.email@example.com
- LinkedIn: [Your Name](https://linkedin.com/in/your-profile)

## 🙏 Acknowledgments

- Google's Gemini API for powering the AI capabilities
- Streamlit for the wonderful web framework
- The open-source community for various supporting libraries

---

**Note**: Remember to replace placeholder text (your-username, your.email@example.com, etc.) with your actual information before using this README.