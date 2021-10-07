import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('doc_tracking')

print("Welcome to Document Status Tracking!")


def user_choice():
    """
    Request the user to choose between new, status and update
    """
    while True:
        print("What would you like to do?\n")
        user_input = input("Enter new/status/update: \n")

        if validate_user_choice(user_input):
            print("Thank you!")
            break

    return user_input

user_choice()



