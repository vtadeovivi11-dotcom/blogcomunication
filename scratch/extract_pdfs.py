import os
from pypdf import PdfReader

pdf_dir = "../documentos_com"
out_dir = "."

for filename in os.listdir(pdf_dir):
    if filename.endswith(".pdf"):
        filepath = os.path.join(pdf_dir, filename)
        out_name = filename.replace(".pdf", ".txt")
        out_path = os.path.join(out_dir, out_name)
        try:
            reader = PdfReader(filepath)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(text)
            pass
        except Exception as e:
            pass
