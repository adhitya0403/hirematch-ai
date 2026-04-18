import pdfplumber
import io
# from docx import Document

def extract_text(file_bytes, filename):
    text = ""

    filename = filename.lower()

    if filename.endswith(".pdf"):
        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""

    # elif filename.endswith(".docx"):
    #     doc = Document(io.BytesIO(file_bytes))
    #     text = "\n".join([p.text for p in doc.paragraphs])

    else:
        raise ValueError("Unsupported file type")

    return text