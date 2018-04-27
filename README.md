# LeumiMail
A utility to open and organize Leumi notification received either by email or by downloading from Leumi site

<<<<<<< HEAD
## Note 
2018 03 13 Leumi discontinued the email service. As such the downloaded option is the only useful one. 

=======
>>>>>>> 1c4c49211bc5f6782a8f769ece84f5a168d648fe
## Usage ##

This utility handles the following use cases:

<<<<<<< HEAD
### zip file processing ###

While in the Leumi web interface - download the new emails from the inbox. The utility was updated to read these zip files, extract the notices into the relevant folder and then process them per account.

### Downloaded notices ###

1. The downloaded notices should be copied to the relevant folder
2. for each html - it is parsed and associated with the relevant account and date


### Email notices ###

Leumi stopped this service 
=======
### Email notices ###


>>>>>>> 1c4c49211bc5f6782a8f769ece84f5a168d648fe

1. Emails are fetched from gmail account
2. from each email the PDF attachment is fetched and downloaded
3. from each PDF the embedded files, usually HTML, are extracted
4. for each html it is parsed and associated with the relevant account and date

<<<<<<< HEAD
=======
### Downloaded notices ###

1. The downloaded notices should be copied to the relevant folder
2. for each html - it is parsed and associated with the relevant account and date

>>>>>>> 1c4c49211bc5f6782a8f769ece84f5a168d648fe

## Environment ###

1. A CSV file describes the various account
2. the files are stored in a structure as follows:
 
	    Script
    	temp /
<<<<<<< HEAD
    		emails # not used anymore
    		attachments # not used anymore
    		downloaded
			zips
=======
    		emails
    		attachments
    		downloaded
>>>>>>> 1c4c49211bc5f6782a8f769ece84f5a168d648fe

