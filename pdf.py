import PyPDF2

with open('dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    page.rotateClockwise(90)   # it's all in memory, not saved
    # print(reader.numPages)
    # print(reader.getPage(0))
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)                 #creating new rotated pdf
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)
    
    