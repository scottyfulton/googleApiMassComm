"""
This is breaking out the main driver/auth for sending/creating email for 
GMAIL API.  The create, create with attachment, and send email 
portions have been broken out and placed in their own package 
named CreateSendEmail.py.

Let's see if this is going to work!!!!

to run:
source /home/scotty/Dropbox/pythonScripts/pyGoogleAPI/api_env/bin/activate
python3 mainMail.py

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
# from oauth2client import client
# from oauth2client import tools
# from oauth2client.file import Storage

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

    # # Call the Gmail API
    # results = service.users().labels().list(userId="me").execute()
    # labels = results.get("labels", [])

    # if not labels:
    #     print("No labels found.")
    # else:
    #     print("Labels:")
    #     for label in labels:
    #         print(label["name"])

# Get the message body from file
# CHANGE THIS FILE FOR ALTERNATE BODY MESSAGE
    bodyName = "textFiles/bodyOfEmail.txt"
    # bodyName = "textFiles/testBody.odt"
    fileHandle = open(bodyName)
    messageBody = fileHandle.read()
    fileHandle.close()

# Get the subject line from file and concat current date
# CHANGE THIS FILE FOR ALTERNATE SUBJECT LINE WITH DATE
    subjectName = "textFiles/subjectLine.txt"
    file2Handle = open(subjectName)
    messageSubject = file2Handle.read()
    subjectMit = messageSubject + ' ' + dateAndTimePractice.now2
    # print (subjectMit)
    file2Handle.close()

# address to send from, authenticated from token.pickle file
    sendAddy = "FAKEMAIL@gmail.com"

# read address list from file and put into list[]
# CHANGE THIS FILE FOR ALTERNATE MAILING LIST

    addressList = "textFiles/scoutEmailList.txt"  #real list
    # addressList = "textFiles/addressList.txt"       #test list
    
    
    # file3Handle = open(addressList)
    addyList = []
# call package forList to iterate thru the addressList.txt
# which returns a populated list into addyList[]  
    addyList = forList.getAddys(addressList)
    # print(addyList)
# for addresses in list create and send message.
    for address in addyList:
        creator = CreateSendEmail.create_message(sendAddy, address, subjectMit, messageBody)
        CreateSendEmail.send_message(service, "me", creator)

if __name__ == "__main__":
    main()
