import PyPDF2
import textract
import  nltk
import sys, os
from MrUtils import Table



def ProcessPDF(Accounts, PDFfile):

    pdfFileObj = open(PDFfile, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print(pdfReader.numPages)
    pageObj = pdfReader.getPage(0)
    pageText = pageObj.extractText()
    if (pageText == ''):
        PDFfilepath = os.getcwd() + '\\'+ PDFfile
        pageText = textract.process(PDFfilepath, method='tesseract', encoding='utf-8')
    print (pageText)
    return


if __name__ == '__main__':
    workingDir = '..\\temp'  # directory where to save attachments (default: current)
    emailsDir = workingDir + "\\emails"
    noticesDir = workingDir + "\\attachments"
    downloadedDir = workingDir + "\\downloaded"
    accountsFile = "ListOfAccounts.csv"

    Accounts = Table()
    csv_fp = open(accountsFile, "rt")
    Accounts.populate_Table(csv_fp)

    os.chdir(downloadedDir)
    if len(sys.argv) == 2: # process the file name
        ProcessPDF(Accounts, sys.argv[1])
