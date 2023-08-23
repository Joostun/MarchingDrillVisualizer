import pdfquery

FILE = "coord_sheets_pg1.pdf"
OUTPUT_XML = "output.xml"

pdf = pdfquery.PDFQuery(FILE)
print(f"Loading {FILE}...")
pdf.load()
print(f"Finished loading {FILE}")

pdf.tree.write(OUTPUT_XML, pretty_print=True)

print(pdf.pq("LTFigure"))