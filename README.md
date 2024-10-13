# LeumiMail
A utility to open and organize Leumi notification received  by downloading from Leumi site

This is release 6.5 which:
1. Upgrade to python 3.13
2. Supports new PDF notices format from Leumi
3. Adds the subject in file name for PDF notices
4. Switched PDF parsing from Tika to pyplumber

Documentation can be seen using PYDOC

## Release History
	2018-04-28 **Release 4.0** Zip file decompressing and good development practices
	2019-05-29 **Release 4.3** Port existing code to Python 3
	2020-06-20 **Release 5.0** remove obsolete code and add PDF parsing
	2021-02-05 **Release 5.1** minor fixes in printing messages
	2021-03-08 **Release 5.2** Support for Union bank PDF. Added command line arg. changed folder structure
	           **Release 5.3** Removing the email option and adding parsing PDF.
	2024-03-11 **Release 6.1** Upgrade to python 3.12
	2024-07-11 **Release 6.2** Supports new PDF notices format from Leumi. Adds the subject in file name for PDF notices. Tika and Java not needed anymore
	2024-10-07 **Release 6.4** date appears in the account line
	2024-10-07 **Release 6.5** Upgrade to python 3.13. 

## Usage ##

This utility handles the following use cases:

### zip file processing ###

While in the Leumi web interface - download the new emails from the inbox. The utility was updated to read these zip files, extract the notices into the relevant folder and then process them per account.

### Downloaded notices ###

1. The downloaded notices should be copied to the relevant folder
2. for each html or pdf - it is parsed and associated with the relevant account and date

## Environment ###

1. A CSV file describes the various account
2. the files are stored in a structure as follows:

	    data
		Source
			temp 
				downloaded
				zips

## Build Guidelines ###

1. Major packages used:
	beautifulsoap

2. See the requirements.txt file.

3. TCL installation for python 3.13 requires the following manual changes:
    - Python installation is C:\Users\<USER>\AppData\Local\Programs\Python\Python313
    - from the tcl folder in the python installation, copy the tcl8.6 folder to lib folder
    - from the tcl folder in the python installation, copy the tk8.6 folder to lib/tcl8.6 folder