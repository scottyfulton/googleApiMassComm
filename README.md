# googleApiScoutMassComm
Mass communication email using google API
###############################################################################
Feb/1/2019  Fultonium
This describes how to use the implemented google API for sending emails 
in my own implementation.
###############################################################################



First, navigate to ~/pyGoogleAPI then activate the py environment by:
    ...$ source api_env/bin/activate
this activates the google api functions and installed drivers.


Run mainMail.py in terminal.
    This file reads from pyGoogleAPI/textFiles/
    1   bodyOfEmail.txt
    2   subjectLine.txt
    3   addressList.txt 
    ***these text files can easily be changed***

    3
    The addressList file path/name is sent to forList.py to read the file 
    and populate a list that is returned to mainMail.py.

    This list is then used in a for loop to iterate thru, creating and sending 
    an email to each addy in the list.  

    2
    The subject line file is text only, but in mainMail.py, the subj line 
    is concatenated with the current date in xx/xx/xx format.  This is done 
    with the help of dateAndTimePractice.py (lots of notes and customizations 
    commented out in this file).

    1
    This file is only read from mainMail.py, and includes the signature.  


Improvements that can be made:
    *Separate the authorization into it's own class, separate from driver.

    *Make driver accept CLI arguments for file names instead of hard coding.

    *issue with certain addresses causing "back end" error with API, 
        rearranging addresses in file helped

