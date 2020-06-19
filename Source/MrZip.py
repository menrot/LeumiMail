# -*- coding: utf-8 -*-
import zipfile
import shutil
import os, sys

#  Extract ZIP from zipsdir to downloadedDir
def ProcessZips(zipsDir, downloadedDir):
    origDir = os.getcwd()
    os.chdir(zipsDir)
    files = [f for f in os.listdir('.') if (os.path.isfile(f) and \
                                            (os.path.splitext(f)[1].lower() == '.zip') and (
                                                        'archive' in os.path.splitext(f)[
                                                    0].lower()))]  # exclude directories and include only zip extension with archive in file name
    for f in files:
        if zipfile.is_zipfile(f):
            zf = zipfile.ZipFile(f, 'r')

            for fileinfo in zf.infolist():
                if fileinfo.compress_type != 0:  # if it is zero - not a file but folder
                    try:
                        with open(downloadedDir + '\\' + fileinfo.filename, "wb") as outputfile:
                            shutil.copyfileobj(zf.open(fileinfo.filename), outputfile)
                            outputfile.close()
                    except IOError:
                        print('Target folder does not exists for file %s' % (fileinfo.filename).decode('cp1255'),
                              file=sys.stderr)
                        pass
        #### NOTE: extract or extracall is not working since file names include hebrew characters
        #            with zipfile.ZipFile(f) as zf:
        #                zf.extractall(downloadedDir)
        else:  # not ZIP
            print('Not a ZIP %s' % f.decode('cp1255'), file=sys.stderr)
        # print ('Zipfile %s processed. Consider deleting it' % f.decode('cp1255'), file=sys.stderr)
        print('Zipfile %s processed. Consider deleting it' % f, file=sys.stderr)
    os.chdir(origDir)
    return


if __name__ == '__main__':
    if len(sys.argv) < 1:
        print("usage MrZip.py")
        exit(1)
    else:
        workingDir = '..\\temp'  # directory where to save attachments (default: current)
        zipsDir = os.path.abspath(workingDir + "\\zips")
        downloadedDir = os.path.abspath(workingDir + "\\downloaded")
        ProcessZips(zipsDir, downloadedDir)
