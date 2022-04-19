import PyPDF2, os

os.chdir('C:\\Users\\burha\\MyPythonScripts\\SamplePDFs')
print(os.getcwd())


pdfFile = open('meetingminutes1.pdf', 'rb')

# IMP: must open in read binary mode using 'rb' keyword argument as PDFs are comple binary files

reader = PyPDF2.PdfFileReader(pdfFile)

# creates a reader object and stores it

print(reader.numPages)

page = reader.getPage(0)

# creates a page object using specified index and stores it

print(page.extractText())

# extracts text from page object

for pageNum in range(reader.numPages):
    print (reader.getPage(pageNum).extractText())

    

# PyPDF2 cannot edit text but can edit pdfs at page level using PyPDF2.PdfFileWriter()

pdfFile1 = open('meetingminutes1.pdf', 'rb')
pdfFile2 = open('meetingminutes2.pdf', 'rb')

readerObj1 = PyPDF2.PdfFileReader(pdfFile1)
readerObj2 = PyPDF2.PdfFileReader(pdfFile2)

writerObj = PyPDF2.PdfFileWriter()

# at this point this doesnt exist on hard drive but in computers memory

for pageNum in range(readerObj1.numPages):
    pageObj1 = readerObj1.getPage(pageNum)
    writerObj.addPage(pageObj1)
    # .addPage method for writer object will append pages to new pdf


for pageNum in range(readerObj2.numPages):
    pageObj2 = readerObj2.getPage(pageNum)
    writerObj.addPage(pageObj2)


# saving writer object using 'wb' mode

outputFile = open('combinedminutes.pdf', 'wb')
writerObj.write(outputFile)

outputFile.close()
pdfFile1.close()
pdfFile2.close()
