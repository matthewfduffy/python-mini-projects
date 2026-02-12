
import glob
import os
from pathlib import Path
from PyPDF2 import PdfWriter, PdfReader

search_dir = Path(r'\path\to\your\folder')
files = ["sample_pdf1.pdf", "sample_pdf2.pdf"]

def merger(output_path, input_paths):
    pdf_writer = PdfWriter()
    for path in input_paths:
        pdf_reader = PdfReader(path)
        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])
    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)



paths = [search_dir / f for f in files]

# Comment line above to get all PDFs in a folder
path = list(search_dir.glob("*.pdf"))


# Prompt for final output PDF name
output_filename = "combined.pdf"

merger(output_filename, paths)