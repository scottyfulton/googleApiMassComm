"""
2/27/19
Scotty Fulton

This is an adaptation to the mainMail.py script for mass emailing, which uses the google API.  This, 
unlike mainMail.py, uses a csv file to receive mailing address with pertinent information.
Very cool, but need to break out the creating message body... and keep the neat 
fill-in-the-blank feature.

to run:
source /home/scotty/Dropbox/pythonScripts/pyGoogleAPI/api_env/bin/activate
python3 mainMailAdvancement_v_2.py

"""

from __future__ import print_function
import httplib2
import os
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from apiclient import discovery

import base64
from email.mime.text import MIMEText
from email.mime.audio import MIMEAudio
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import mimetypes
import dateAndTimePractice

import forList
import CreateSendEmail
# import AdventureSpreadReaderTester

# If modifying these scopes, delete the file token.pickle.
SCOPES = ["https://mail.google.com/"]
# SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


##########################################################################
def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    service = build("gmail", "v1", credentials=creds)


# Get the subject line from file and concat current date
# CHANGE THIS FILE FOR ALTERNATE SUBJECT LINE WITH DATE
    subjectName = "textFiles/subjectLine.txt"
    file2Handle = open(subjectName)
    messageSubject = file2Handle.read()
    subjectMit = messageSubject + ' ' + dateAndTimePractice.now2
    # print (subjectMit)
    file2Handle.close()

# address to send from, authenticated from token.pickle file
    sendAddy = "fakeEmail@gmail.com"

# this is where the new shit is
    import csv

    rowHeader = []
    # really cool way to get file path for file name in folder name
    filename = os.path.abspath( os.path.join("textFiles", "AdventureSpreadsheetCSV.csv") )
    # print(filename)
    addys = []
    with open(filename, 'r') as fin:
        header1 = fin.readline().strip().split(';')

        entries = []
        for line in fin:
            parts = line.strip().split(';')
            row = dict()
            for i, h in enumerate(header1):
                row[h] = parts[i]
            entries.append(row)
            addys.append(parts[1])  #adds email addy to addys[]

    # this prints the email that the message confirmation goes with
    for e in entries:
        outfile = open('bodyOfEmail.txt', 'w')
        addressToSendTo = addys.pop(0)
        print('\n')
        print (addressToSendTo)
        # uses ''' blah blah blah ''' and keeps formatting between delimiters
        outfile.write('''
Hello {0} family, 

    This is to inform you of {1}'s progress on his Adventure 
completion towards the Tiger scouts.  The Adventures that 
have been achieved will show the date when they were completed.  
Adventures with no dates haven't been completed yet.

Required Adventures:
\tLions Honor - {2}
\tAnimal Kingdom - {3}
\tFun on the Run - {4}
\tKing of the Jungle - {5}
\tMountain Lion - {6}

Elective Adventures:
\tBuild it up, knock it down - {7}
\tGizmos and Gadgets - {8}
\tI’ll do it myself - {9}
\tOn your mark - {10}
\tPick my path - {11}
\tReady set grow - {12}
\tRumble in the jungle - {13}

    Please review and confirm that these match your records 
(and check their awarded belt loops), and if you have any 
questions please let me know.  We still have plenty of
time to get, at a minimum, the required ones completed.

Thank you for your time, 

Scotty Fulton 
Lion Den Leader 
Pack 346  
        '''.format(
            # this is where all the {x}'s are repopulated fromt he csv file.
        e['LNAME'], e['SCOUT'], e['Lions Honor'], e['Animal Kingdom'], e['Fun on the Run'], e['King of the Jungle'],e['Mountain Lion'], e['Build it up, knock it down'], e['Gizmos and Gadgets'], e['I’ll do it myself'],e['On your mark'], e['Pick my path'], e['Ready set grow'], e['Rumble in the jungle']))
        outfile.close()

        # opens written file and attaches to body tag
        bodyName = "bodyOfEmail.txt"
        # bodyName = "textFiles/testBody.odt"
        fileHandle = open(bodyName)
        messageBody = fileHandle.read()
        fileHandle.close()
        # makes the magic, creates the email
        creator = CreateSendEmail.create_message(sendAddy, addressToSendTo, subjectMit, messageBody)
        CreateSendEmail.send_message(service, "me", creator)


if __name__ == "__main__":
    main()
