from PyPDF2 import PdfReader


reader = PdfReader("coord_sheets_pg1.pdf")
page = reader.pages[0]
rawtext = page.extract_text()


with open("text_output.txt", "w") as file:
  file.write(page.extract_text())