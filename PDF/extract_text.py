from PyPDF2 import PdfFileWriter, PdfFileReader

file = open("recap.pdf", "rb")
reader = PdfFileReader(file)

page0 = reader.getPage(0)
text = page0.extractText()

text = text.replace("Ò", "\"").replace("‘", "è").replace("”", "é").replace("‹", "à")

print(text)
file.close()