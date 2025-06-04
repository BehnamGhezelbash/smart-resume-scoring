

import fitz
import os


def extract_text_from_pdf(pdf_path):
    """
    Extracts and returns all text from a PDF file.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: Extracted text.
    """
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text.strip()
    except Exception as e:
        print(f"Failed to extract text from {pdf_path}: {e}")
        return ""


def parse_all_resumes(resume_folder):
    """
    Parses all PDF resumes in a given folder.

    Args:
        resume_folder (str): Path to the folder containing PDF resumes.

    Returns:
        dict: A dictionary mapping resume filenames to extracted text.
    """
    resumes = {}
    for filename in os.listdir(resume_folder):
        if filename.lower().endswith(".pdf"):
            path = os.path.join(resume_folder, filename)
            resumes[filename] = extract_text_from_pdf(path)
    return resumes
