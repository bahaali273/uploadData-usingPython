import PyPDF2

with open("smart sketcher.pdf", "rb") as file:
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
#pn => page number
    for pn in range(len(pdf_reader.pages)):
        page =pdf_reader.pages[pn]
        text +=page.extract_text()

print(text)