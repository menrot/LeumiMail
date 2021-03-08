# LeumiMail
A utility to open and organize Leumi notification received  by downloading from Leumi site

This is release 5.x which:
1. finaly removes the email option
2. Adding PDF parsing as Leumi changed that many notices are PDF 

Documentation can be seen using PYDOC


## Release History
	2018-04-28 **Release 4.0** Zip file decompressing and good development practices
	2019-05-29 **Release 4.3** Port existing code to Python 3
	2020-06-20 **Release 5.0** remove obsolete code and add PDF parsing
	2021-02-05 **Release 5.1** minor fixes in printing messages
	2021-03-08 **Release 5.2** Support for Union bank PDF. Added command line arg. changed folder structure

## Usage ##

This utility handles the following use cases:

### zip file processing ###

While in the Leumi web interface - download the new emails from the inbox. The utility was updated to read these zip files, extract the notices into the relevant folder and then process them per account.

### Downloaded notices ###

1. The downloaded notices should be copied to the relevant folder
2. for each html or pdf - it is parsed and associated with the relevant account and date



### Downloaded notices ###

1. The downloaded notices should be copied to the relevant folder
2. for each html - it is parsed and associated with the relevant account and date

## Environment ###

1. A CSV file describes the various account
2. the files are stored in a structure as follows:

	    Script
			temp /
				downloaded
				zips

