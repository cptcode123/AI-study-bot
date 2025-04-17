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


def detect_file_type(file_path: str) -> str:
    """
    Determines the file type based on its extension.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The file type (e.g., 'pdf', 'docx', 'txt').
    """
    if file_path.endswith('.pdf'):
        return 'pdf'
    elif file_path.endswith('.docx'):
        return 'docx'
    elif file_path.endswith('.txt'):
        return 'txt'
    else:
        raise ValueError("Unsupported file type")
    

def parser_call(file_path: str) -> str:
    if detect_file_type(file_path) == 'pdf':
        # Call the PDF parser
        return parse_pdf(file_path)
    elif detect_file_type(file_path) == 'docx':
        # Call the DOCX parser
        return parse_docx(file_path)
    elif detect_file_type(file_path) == 'txt':
        # Call the TXT parser
        return parse_txt(file_path)

def chunk_text(text: str, chunk_size: int = 5000) -> List[str]:
    """
    Splits text into smaller chunks for processing.

    Args:
        text (str): The text to be chunked.
        chunk_size (int): The maximum size of each chunk.

    Returns:
        List[str]: A list of text chunks.
    """

def parse_pdf():
    '''
    Parses PDF files to extract text.
    '''
    pass

def parse_docx():
    '''
    Parses DOCX files to extract text.
    '''
    pass

def parse_txt():
    '''
    Parses TXT files to extract text.
    '''
    pass



def clean_text():
    '''
    Cleans the extracted text for better readability and processing.
    '''
    pass


def extract_metadata():
    '''
    Extracts metadata from the document, such as title, author, and creation date.
    '''
    pass

def generate_embedding():
    '''
    Generates embeddings for the text chunks using a pre-trained model.
    '''
    pass


def process_file():
    '''
    Main function to process the uploaded file.
    - Detects file type
    - Parses the file
    - Cleans the text
    - Optionally chunks the text
    - Extracts metadata
    - Generates embeddings
    '''
    pass
