import pdfplumber

pdf = 'example_pdf.pdf'
txt = 'example_text.txt'

with pdfplumber.open(pdf) as source:
    with open(txt, 'w', ecoding='utf-8') as extract:
        for pg_obj in source.pages:
            txt_obj = pg_obj.extract_text()
            extract.write(txt_obj)