import gspread
from google.oauth2.service_account import Credentials
import datetime
from datetime import timedelta

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("doc_tracking")


def user_choice_task():
    """
    Request the user to choose an action to perform from new, status and update
    Calls function to validate the user input
    Returns variable user_input with the chosen action
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
            request_update_by()
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


def create_rows(data):
    if data == "new":
        print(f"Please enter new user name:\n")
        new_fname = input("First name \n")
        new_lname = input("Last name \n")
        print(f"Please enter new user role:\n")
        print(f"Enter as follows: PI/Sub-I/SC\n")
        new_role = input("Role \n")
        new_date = add_new_date()
        deadline_date = calc_deadline(new_date)

        first_new_row = []
        first_new_row.extend((new_fname, new_lname, new_role, deadline_date, "Planned"))
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


def add_new_date():
    """
    Request user to provide start date in specific format
    Returns the date provided
    """
    print(f"Please enter start date:\n")
    print(f"Use date format YYYY-MM-DD:\n")
    print(f"Example 2021-10-07:\n")
    new_date = input("Date \n")
    return new_date


def calc_deadline(date):
    """
    Converts user input datestring to datetime using strptime method
    Calculates new deadline 15 days ahead using timedelta
    """
    date_time_str = date
    date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d')
    deadline_date = date_time_obj + timedelta(15)
    deadline_date_string = deadline_date.strftime("%Y-%m-%d")
    print(deadline_date)
    print(deadline_date_string)
    return deadline_date_string


def add_doc_rows(data, worksheet):
    """
    Receives a list of lists with staff data to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    print(f"Adding staff and documents to {worksheet} worksheet...\n")
    for row in all_new_rows:
        worksheet_to_update = SHEET.worksheet(worksheet)
        worksheet_to_update.append_row(row)
    print(f"{worksheet} worksheet updated!\n")


def request_update_by():
    
    print(f"Please chose filter for update:\n")
    print(f"By role, by deadline or list all\n")
    update_filter = input("role/deadline/all \n")
    print(f"You picked {update_filter}")
    return update_filter

def request_update_role():
    print(f"Please chose role update:\n")
    update_role = input("PI/Sub-I/SC \n")
    print(f"You picked {update_role}")
    return update_role

    
def print_list():
    """
    Calls and uses return values from request_update_role function and
    add_row_numbers function.
    Returns chosen filtered list including the row index to be updated
    """
    all_rows = add_row_number()
    update_role = request_update_role()
    print(update_role)
    if update_role == "SC":
        filtered_list_sc = list(filter(lambda x: "SC" in x, all_rows))
        print(filtered_list_sc)
        return filtered_list_sc
    elif update_role == "PI":
        filtered_list_pi = list(filter(lambda x: "PI" in x, all_rows))
        print(filtered_list_pi)
        return filtered_list_pi
    elif update_role == "Sub-I":
        filtered_list_subi = list(filter(lambda x: "Sub-I" in x, all_rows))
        print(filtered_list_subi)
        return filtered_list_subi
    
        

def add_row_number():
    """
    Pulls all rows from the doc collection worksheet
    Iterates through the list of lists, appending an increasing row 
    number to the end of each list, returns a full list of lists
    """
    all_rows = SHEET.worksheet("doc_collection").get_all_values()
    index = 1
    for row in all_rows:
        row.append(index)
        index = index + 1
    return all_rows
   

def update_doc_status(worksheet):
    print("What row number is to be update?")
    print("Row number is indicated last in the row") 
    row_number = input("Row number:\n")
    print("Add new document status as requested /sent/ complete")
    new_status = input("New status:\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.update_cell(row_number, 5, new_status)
    print(f"{worksheet} worksheet updated with new document status!\n")



print("Welcome to Document Status Tracking!")
update_doc_status("doc_collection")
#request_update_by()
#request_update_role()
#role_filter = print_list()
#filter_by_role(role_filter)

#filter_by_role()
#user_input = user_choice_task()
#request_update_by()
#all_new_rows = create_rows(user_input)
#add_doc_rows(all_new_rows, "doc_collection")
#update_doc_status(user_input)
#filter_by_role()
#all_rows = add_row_number()
#print(all_rows)
#print_list()
#print(filtered_list_sc)



