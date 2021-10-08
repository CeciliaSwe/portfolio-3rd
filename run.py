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
SHEET = GSPREAD_CLIENT.open("doc_tracking")

print("Welcome to Document Status Tracking!")


def user_choice():
    """
    Request the user to choose an action to perform from new, status and update
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


def add_new_staff(data):
    if data == "new":
        print(f"Please enter new user name:\n")
        new_fname = input("First name \n")
        new_lname = input("Last name \n")
        print(f"Please enter new user role:\n")
        print(f"Enter as follows: PI/Sub-I/SC\n")
        new_role = input("Role \n")
        first_new_row = []
        first_new_row.extend((new_fname, new_lname, new_role))
        second_new_row = first_new_row.copy()
        third_new_row = first_new_row.copy()
        first_new_row.append("CV")
        second_new_row.append("GCP Certificate")

    if new_role == "PI" or new_role == "Sub-I":
        third_new_row.append("Financial Disclosure")  
    elif new_role == "SC":
        third_new_row.append("IATA Certificate")
    all_new_rows = [first_new_row, second_new_row, third_new_row]
    print(all_new_rows)
    return all_new_rows


def update_doc_rows(data, worksheet):
    """
    Receives a list of lists with staff data to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    print(f"Adding staff and documents to {worksheet} worksheet...\n")
    for row in all_new_rows:
        worksheet_to_update = SHEET.worksheet(worksheet)
        worksheet_to_update.append_row(row)
    print(f"{worksheet} worksheet updated!\n")


user_input = user_choice()
all_new_rows = add_new_staff(user_input)
update_doc_rows(all_new_rows, "doc_collection")


