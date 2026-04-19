import pdfplumber
import io
# from docx import Document

def text_extractor(file_bytes, filename):
    text = ""
    filename = filename.lower()

    if filename.endswith(".pdf"):
        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""

    else:
        raise ValueError("Unsupported file type")

    return text