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
    Request the user to choose an action to perform between new, status and update
    Calls function to validate the user input
    Returns variable user_inout with the chosen action
    """
    while True:
        print("What would you like to do?\n")
        user_input = input("Enter new/status/update: \n")

        if validate_user_choice(user_input):
            print("Thank you!")
            break

    return user_input

def validate_user_choice(input):
    """
    Inside the try, run a series of if statements to check user input
    Raises ValueError if strings do not match the given options.
    """
    try:
        if input == "update":
            print(f"You picked {input}")
        elif input == "new":
            print(f"You picked {input}")
        elif input == "status":
            print(f"You picked {input}")
        else:
            raise ValueError(
                f"You need to pick one of the given options"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


user_input = user_choice()



