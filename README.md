# 📚 Smart Study Assistant

An AI-powered web application that transforms study materials into interactive learning tools. Upload textbooks, lecture notes, or slides and get flashcards, quizzes, summaries, and a conversational chatbot to help you study more efficiently.

---

## 🚀 Features

### 📄 Document Upload
- Supports PDF, DOCX, and TXT formats
- Extracts and preprocesses text for downstream tasks
- Automatically chunks large documents for better AI handling

### 🧠 AI-Powered Q&A Chatbot
- Ask questions directly about your uploaded material
- Built with Retrieval-Augmented Generation (RAG)
- Uses vector embeddings (FAISS or ChromaDB) + OpenAI or LLaMA-based LLMs

### 📝 Flashcard Generator
- Automatically creates question-answer pairs from your content
- Editable flashcards interface with swipe/flip interaction

### 🧪 Quiz Builder
- Generates multiple choice quizzes using document content
- Provides instant feedback and scoring

### 📚 Smart Summarizer
- Summarizes entire documents or specific sections
- Supports multiple summary lengths (brief, standard, detailed)

---

## 🧰 Tech Stack

- **Frontend:** Streamlit (or React + Flask)
- **Backend:** Python, LangChain, OpenAI API
- **Document Parsing:** PyMuPDF, `python-docx`, `pdfplumber`
- **Vector Store:** FAISS or ChromaDB
- **Embeddings:** OpenAI, HuggingFace Transformers
- **Extras:** Tiktoken (for chunking), spaCy/NLTK (for NLP)

---

## 📂 Project Structure
smart-study-assistant/ │ ├── app/ # Main Streamlit or Flask app │ ├── pages/ # Flashcards, quiz, summary views │ ├── components/ # Reusable UI elements │ └── main.py │ ├── backend/ │ ├── document_parser.py # PDF/DOCX/TXT extractors │ ├── rag_pipeline.py # LangChain or custom retrieval logic │ ├── quiz_generator.py # AI-based quiz system │ ├── summarizer.py │ └── flashcard_creator.py │ ├── static/ │ └── sample_docs/ # Example study files │ ├── requirements.txt └── README.md



---

## 🛠️ Setup & Installation

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/smart-study-assistant.git
cd smart-study-assistant

```
### 2. Create a virtual environment & install dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Add API keys
Create a .env file and add your OpenAI key:
```ini
OPENAI_API_KEY=your_openai_key_here
```

### 4. Run the app
```bash
streamlit run app/main.py
```

## 🌐 Deployment
You can deploy ths app to:
- Render: for full backend + frontend
- VercelL for frontend (React version)
- Hugging Face Spaces: for Streamlit or Gradio

## ✍️ Author
Daniel Igwe
AI & Web Dev Enthusiast

## 📜 License
Feel free to fork, adapt, and build on it!


