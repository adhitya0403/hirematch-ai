import fitz  # PyMuPDF

def text_extractor(file_bytes, filename):
    if not filename.lower().endswith(".pdf"):
        raise ValueError("Unsupported file type")

    text = ""

    with fitz.open(stream=file_bytes, filetype="pdf") as doc:
        for page in doc:
            text += page.get_text() + "\n"

    return text