import PyPDF2

# create object
file = open('filename.pdf', 'rb')

# create pdf reader object
file_reader = PyPDF2.PdfFileReader(file)
fields = file_reader.getFields()
fields