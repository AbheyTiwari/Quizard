from PyPDF2 import PdfReader
import docx
import pandas as pd

def extract_text(file):
    filename = file.filename.lower()
    if filename.endswith(".pdf"):
        reader = PdfReader(file.file)
        return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

    elif filename.endswith(".docx"):
        doc = docx.Document(file.file)
        return "\n".join([p.text for p in doc.paragraphs])

    elif filename.endswith(".xlsx"):
        dfs = pd.read_excel(file.file, sheet_name=None)
        return "\n".join([df.to_string() for df in dfs.values()])

    elif filename.endswith(".txt"):
        return file.file.read().decode("utf-8")

    return "Unsupported file type."
