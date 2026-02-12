import PyPDF2

# creates object, change filename to pdf file
file = open('filename.pdf', 'rb')

# creates pdf reader object
fileReader = PyPDF2.PdfReader(file)
fields = fileReader.get_fields()
fields