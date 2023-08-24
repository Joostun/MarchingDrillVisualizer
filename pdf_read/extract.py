from PyPDF2 import PdfReader


reader = PdfReader("coord_sheets_pg1.pdf")
page = reader.pages[0]
with open("text_output.txt", "w") as file:
  file.write(page.extract_text())