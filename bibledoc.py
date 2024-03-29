from __future__ import print_function

import os.path
import sys

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from verse_requests import GetRequests

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.file',
          'https://www.googleapis.com/auth/documents']

DEFAULT_TITLE = "Untitled Document"

def main():
    if len(sys.argv) > 3:
        usage_message = "Command line input: python3 bibledoc.py filename [document_title]\n"
        print(usage_message, file=sys.stderr)
        return
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
        document_title = DEFAULT_TITLE
    elif len(sys.argv) == 3:
        filename = sys.argv[1]
        document_title = sys.argv[2]
    else:
        filename = input("Enter the name of the file you want to create your document from: ")

    if os.path.isfile(filename):
        document_title = input("Enter your Google document's title: ")
    else:
        print("Please use a valid file name")

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('docs', 'v1', credentials=creds)

        body = {
            'title': document_title
        }

        doc = service.documents() \
            .create(body=body).execute()
        print(f"Created document with title: {doc.get('title')}")

        DOCUMENT_ID = doc.get('documentId')
        print(DOCUMENT_ID)
        requests = GetRequests(filename)
        result = service.documents().batchUpdate(documentId=DOCUMENT_ID, \
                                                body={'requests': requests}) \
                                                    .execute()
    except HttpError as err:
        print(err)

if __name__ == '__main__':
    main()