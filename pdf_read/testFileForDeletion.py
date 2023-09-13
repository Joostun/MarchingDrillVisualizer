from PyPDF2 import PdfReader

pdf_reader = PdfReader("pdf_read\Fantasmic Coordinate Sheets.pdf")
text_list = []
raw_text = ""
page = pdf_reader.pages[0]
for pdfPage in pdf_reader.pages:
    raw_text = raw_text + pdfPage.extract_text()

sheets = raw_text.split("Printed:")[:-1]

print(len(sheets))