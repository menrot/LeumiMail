# -*- coding: utf-8 -*-
#
# Extract Embedded object if PDF
# based on dumppdf.py - dump pdf contents in XML format.
#
import sys, os.path, re
from pdfminer.psparser import PSKeyword, PSLiteral, LIT
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument, PDFNoOutlines, PDFXRef, PDFXRefFallback
from pdfminer.pdftypes import PDFObjectNotFound, PDFValueError
from pdfminer.pdftypes import PDFStream, PDFObjRef, resolve1, stream_value
from random import *
# from pdfminer.pdfpage import PDFPage
# from pdfminer.utils import isnumber


# extractembedded
LITERAL_FILESPEC = LIT('Filespec')
LITERAL_EMBEDDEDFILE = LIT('EmbeddedFile')
def extractembedded(fname, password='', extractdir=None, emailsDir=None):
    def extract1(obj):
        filename = os.path.basename(obj['F'])
#       filename = os.path.basename(obj['UF'] or obj['F'])
        fileref = obj['EF']['F']
        fileobj = doc.getobj(fileref.objid)
        if not isinstance(fileobj, PDFStream):
            raise PDFValueError(
                'unable to process PDF: reference for %r is not a PDFStream' %
                (filename))
        if fileobj.get('Type') is not LITERAL_EMBEDDEDFILE:
            raise PDFValueError(
                'unable to process PDF: reference for %r is not an EmbeddedFile' %
                (filename))
        file_name, extension = os.path.splitext(fname)
        path = os.path.join(extractdir, file_name + " " + filename)
        while os.path.exists(path):
            path = os.path.join(extractdir, file_name + " " + str(randint(1,100)) + " " + filename)
            print >> sys.stderr, "file exists, create random name %s" % path
        # print >>sys.stderr, 'extracting: %r' % path
        out = file(path, 'wb')
        out.write(fileobj.get_data())
        out.close()
        return

    fp = file(os.path.join(emailsDir, fname), 'rb')
    parser = PDFParser(fp)
    doc = PDFDocument(parser, password)
    for xref in doc.xrefs:
        if type(xref) == PDFXRef:   # Ignore PDFXreffallback. Not sure what it is.
            for objid in xref.get_objids():
                obj = doc.getobj(objid)
                if isinstance(obj, dict) and obj.get('Type') is LITERAL_FILESPEC:
                    extract1(obj)
    return






