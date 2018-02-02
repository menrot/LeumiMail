# LeumiMail
A utility to open and organize Leumi notification received either by email or by downloading from Leumi site

## Usage ##

This utility handles the following use cases:

### Email notices ###



1. Emails are fetched from gmail account
2. from each email the PDF attachment is fetched and downloaded
3. from each PDF the embedded files, usually HTML, are extracted
4. for each html it is parsed and associated with the relevant account and date

### Downloaded notices ###

1. The downloaded notices should be copied to the relevant folder
2. for each html - it is parsed and associated with the relevant account and date


## Environment ###

1. A CSV file describes the various account
2. the files are stored in a structure as follows:
 
	    Script
    	temp /
    		emails
    		attachments
    		downloaded

