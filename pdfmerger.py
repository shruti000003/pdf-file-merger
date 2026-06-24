from pypdf import PdfWriter

writer = PdfWriter()

pdfs = ["file1.text", "file2.text"]

for pdf in pdfs:
      writer.append(pdf)

writer.write("merged.pdf")
writer.close()
print("pdfs merged successfully into 'merged.pdf'")      