from PyPDF2 import PdfFileWriter, PdfFileReader

# ---------- PyPDF ----------
# Read
# Extract (text)
# Write
#       - Combine
#       - Rotation, Superimpose
#       - Cannot: Add text or images

output_content = PdfFileWriter()

file_pdf_presentation = open("presentation.pdf", "rb")
file_pdf_recap = open("recap.pdf", "rb")

reader_presentation = PdfFileReader(file_pdf_presentation)
reader_recap = PdfFileReader(file_pdf_recap)

print(f"Number pages from recap file: {reader_recap.getNumPages()}")

output_content.addPage(reader_presentation.getPage(0)) # .rotateClockwise(90)

for i in range(1, reader_recap.getNumPages()):
    output_content.addPage(reader_recap.getPage(i))


output_file = open("combined.pdf", "wb")
output_content.write(output_file)

output_file.close()
file_pdf_presentation.close()
file_pdf_recap.close()


