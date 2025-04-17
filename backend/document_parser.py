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

from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class ProcessedChunk:
    """
    Represents a chunk of processed text from a document.
    
    Attributes:
        text (str): The extracted text from the document.
        metadata (dict): Additional information about the chunk, such as page number or section title.
    """
    book: str
    chunk_numeber: int
    title: str
    summary: str
    content: str
    metadata: Dict[str, Any]
    embedding: List[float]


def chunk_text(text: str, chunk_size: int = 5000) -> List[str]:
    """
    Splits text into smaller chunks for processing.

    Args:
        text (str): The text to be chunked.
        chunk_size (int): The maximum size of each chunk.

    Returns:
        List[str]: A list of text chunks.
    """
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end  = min(start + chunk_size, text_length)

        # At the end of the text
        if end >= text_length:
            chunks.append(text[start:].strip())
            break
        