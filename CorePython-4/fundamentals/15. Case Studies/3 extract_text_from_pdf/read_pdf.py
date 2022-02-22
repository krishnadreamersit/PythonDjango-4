# Read PDF
import PyPDF2  # pip install PyPDF2
pdfObject = open(r"sample.pdf", 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfObject)
if(pdfReader.numPages>0):
    current_page=0;
    while current_page<pdfReader.numPages:
        print("Content of "+str(current_page+1)+" ----------------")
        pageObject = pdfReader.getPage(current_page)
        print(pageObject.extractText())
        current_page+=1
pdfObject.close()

# NLP - Natural Language Processing