import os

# Service type constants for Google Services
SHEETS = 1
DOCS = 2
DRIVE = 3

USER_EMAIL = 'editor@writershark.com'

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive',
          'https://www.googleapis.com/auth/gmail.send']

# Trello Constants
PARAMS = {
    'key': os.environ.get('TRELLO_API_KEY'),
    'token': os.environ.get('TRELLO_TOKEN'),
    'idList': '6200d4ebdb706677ca30f0f6'
}

HEADERS = {
    "Accept": "application/json"
}

CREATE_CARD_URL = 'https://api.trello.com/1/cards'
SURPLUS_CUSTOM_FIELD_ID = '6200b6d75c3f8a2161df7b30'

# Date Time Related Things
DATE_FORMAT = '%Y-%m-%d'

CALENDAR_DETAILS_SPREADSHEET_ID = '12o73YDTAuCeb2n-w_pwPfT-f5bDdu26G7eeRQC0dVlU'
LEAVE_ADDITION_SHEET_RANGE = 'Leave Addition!A2:B'
MONTH_END_SPREADSHEET_ID = '1HfVEbDG_kBKGd3U_x1OZYJUuiKNIGc-gEJiqe64H50k'
MONTH_END_SHEET_RANGE = 'March 2022!A2:E'
