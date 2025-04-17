"""
📄 document_parser.py

Handles file uploads and text extraction for supported formats: PDF, DOCX, and TXT.

Key Functions:
- Detects file type and applies appropriate parser
- Extracts clean, structured text from user-uploaded documents
- Optionally chunks long documents for downstream AI processing (e.g., embeddings)

Libraries Used:
- PyMuPDF or pdfplumber (for PDFs)
- python-docx (for Word files)
- Standard Python I/O (for plain text)

This module acts as the first stage in the Smart Study Assistant pipeline, transforming raw documents into usable text for summarization, flashcard generation, and Q&A.
"""
