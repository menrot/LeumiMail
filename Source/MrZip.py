# -*- coding: utf-8 -*-
import zipfile
import shutil
import os, sys

def ProcessZips(zipsDir, downloadedDir):
    origDir = os.getcwd()
    os.chdir(zipsDir)
    files = [f for f in os.listdir('.') if (os.path.isfile(f) and os.path.splitext(f)[1].lower() == '.zip')]  # exclude directories and include only zip extension
    for f in files:
        if zipfile.is_zipfile(f):
            zf = zipfile.ZipFile(f, 'r')
            for fileinfo in zf.infolist():
                with open(downloadedDir + '\\' + fileinfo.filename, "wb") as outputfile:
                    shutil.copyfileobj(zf.open(fileinfo.filename), outputfile)
                    outputfile.close()
#### NOTE: extract or extracall is not working since file names include hebrew characters
#            with zipfile.ZipFile(f) as zf:
#                zf.extractall(downloadedDir)
        else: #not ZIP
            print 'Not a ZIP %s' % f
    os.chdir(origDir)
    return

if __name__ == '__main__':
    if len(sys.argv) <1:
        print "usage test.py"
        exit(1)
    else:
        workingDir = '..\\temp'  # directory where to save attachments (default: current)
        zipsDir = os.path.abspath(workingDir + "\\zips")
        downloadedDir = os.path.abspath(workingDir + "\\downloaded")
        ProcessZips(zipsDir, downloadedDir)




