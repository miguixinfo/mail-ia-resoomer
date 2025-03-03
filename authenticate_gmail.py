import os
import pickle
import google.auth.transport.requests
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
# Define the SCOPES (Permissions we request from Gmail)
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

def authenticate_gmail():
    """
    Authenticates the user with Gmail API using OAuth 2.0.
    This function checks for existing credentials stored in a token.pickle file.
    If the credentials are not found or are invalid/expired, it initiates the OAuth 2.0
    flow to obtain new credentials and saves them to the token.pickle file for future use.
    Returns:
        google.oauth2.credentials.Credentials: The authenticated credentials for Gmail API.
    """
    creds = None
    
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(google.auth.transport.requests.Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    return creds

def get_gmail_service():
    creds = authenticate_gmail()
    return build("gmail", "v1", credentials=creds)

if __name__ == "__main__":
    service = get_gmail_service()
    print("Authentication successful. Ready to read emails.")
