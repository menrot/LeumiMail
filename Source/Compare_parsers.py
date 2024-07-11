import os, sys
from PyPDF2 import PdfReader
import pymupdf # imports the pymupdf library
import pdfplumber

def parse_pydef2(oldf, newf):
    print('\n\nparse_pydef2')
    print('oldf: ', oldf)

    reader = PdfReader(oldf)
    meta = reader.metadata
    print("Total Pages: ", len(reader.pages))
    # All of the following could be None!
    print("Author: ", meta.author)
    print("Creator: ", meta.creator)
    print("Producer: ", meta.producer)
    print("Subject: ", meta.subject)
    print("Title: ", meta.title)

    page = reader.pages[0]

    safe_text = page.extract_text()

    loc = safe_text.find('מס. לקוח')

    print('loc: ', loc)
    print('safe_text: ', safe_text)

    print('\nnewf: ', newf)
    reader = PdfReader(newf)
    meta = reader.metadata
    print("Total Pages: ", len(reader.pages))
    # All of the following could be None!
    print("Author: ", meta.author)
    print("Creator: ", meta.creator)
    print("Producer: ", meta.producer)
    print("Subject: ", meta.subject)
    print("Title: ", meta.title)

    page = reader.pages[0]

    safe_text = page.extract_text()

    loc = safe_text.find('מס. לקוח')

    print('loc: ', loc)
    print('safe_text: ', safe_text)

    return


def parse_pymupdf(oldf, newf):
    print('\n\nparse_pymupdf')
    print('oldf: ', oldf)

    doc = pymupdf.open(oldf)
    for page in doc:
        safe_text = page.get_text()

    loc = safe_text.find('מס. לקוח')

    print('loc: ', loc)
    print('safe_text: ', safe_text)

    print('\nnewf: ', newf)
    doc = pymupdf.open(newf)
    for page in doc:
        safe_text = page.get_text()

    loc = safe_text.find('מס. לקוח')

    print('loc: ', loc)
    print('safe_text: ', safe_text)

    return

def parse_pdfplumber(oldf, newf):
    print('\n\nparse_pdfplumber')
    print('oldf: ', oldf)


    with pdfplumber.open(oldf) as pdf:
        # Extract the text
        pages = pdf.pages
        safe_text = pages[0].extract_text()

    loc = safe_text.find('חוקל .סמ')
    print('loc: ', loc)

    print('safe_text: ')
    for line in safe_text.split('\n'):
        print(line)


    print('\nnewf: ', newf)
    with pdfplumber.open(newf) as pdf:
        # Extract the text
        pages = pdf.pages
        safe_text = pages[0].extract_text()

    loc = safe_text.find('חוקל .סמ')
    print('loc: ', loc)

    print('safe_text: ')
    for line in safe_text.split('\n'):
        print(line)

    return


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("usage compare_parsers dir old new")
        exit(1)
    else:
        origDir = os.getcwd()
        os.chdir(sys.argv[1])

#        parse_pydef2(sys.argv[2], sys.argv[3])
#       parse_pymupdf(sys.argv[2], sys.argv[3])
        parse_pdfplumber(sys.argv[2], sys.argv[3])
        exit(0)
