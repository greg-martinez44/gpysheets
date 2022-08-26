from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


class Connection:

    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    SCRIPT_DIR = Path(__module__).parent.absolute()
    CREDS_FILE_PATH = Path(SCRIPT_DIR, "resources", "credentials.json")
    TOKEN_FILE_PATH = Path(SCRIPT_DIR, "resources", "token.json")

    def __init__(self):
        self.creds = None
        if Connection.TOKEN_FILE_PATH.exists():
            self.creds = Credentials.from_authorized_user_file(
                str(Connection.TOKEN_FILE_PATH), Connection.SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    str(Connection.CREDS_FILE_PATH), Connection.SCOPES)
                self.creds = flow.run_local_server(port=8080)
            # Save the credentials for the next run
            with open(Connection.TOKEN_FILE_PATH, 'w') as token:
                token.write(self.creds.to_json())

    def cred_file_path(self):
        return str(Connection.CREDS_FILE_PATH)

    def token_file_path(self):
        return str(Connection.TOKEN_FILE_PATH)

    def get_service(self):
        return build('sheets', 'v4', credentials=self.creds)
