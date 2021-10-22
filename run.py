import datetime
from datetime import timedelta
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


def input_action():
    """
    Requests the user to choose an action to perform from new, status and update.
    Calls function to validate the user input based on numbered options.
    Uses a while loop to keep running until input is valid.
    Returns variable user_input with the chosen action
    """
    while True:
        print("Please select action:\n")
        print("1 : New      Add site staff details to generate rows in Document Tracking")
        print("2 : Update   Update status of existing row in Document Tracking")
        print("3 : Status   Print all existing rows with status in Document Tracking\n")
        user_input = input("Action: \n")
        options = ["1", "2", "3"]

        if validate_user_input(user_input, options):
            break

    return user_input


def input_role():

    """
    Requests the user to choose a role from options.
    Calls function to validate the user input based on numbered options.
    Uses a while loop to keep running until input is valid.
    Converts the numbered choice to a string and returns variable new_role
    with the string generated.
    """

    while True:
        print("Please select role:\n")
        print("1 : PI       Principal Investigator")
        print("2 : Sub-I    Sub-Investigator")
        print("3 : SC       Study Coordinator \n")
        options = ["1", "2", "3"]
        new_role = input("Role: \n")

        if validate_user_input(new_role, options):
            print("Thank you for providing role!")
            break
    
    if new_role == "1":
        new_role = "PI"
    elif new_role == "2":
        new_role = "Sub-I"
    elif new_role == "3":
        new_role = "SC"

    return new_role


def create_rows():
    """
    Requests user input on name, role.
    Calls function to input date.
    Uses while loops to run until input is valid and calls functions to validate input.
    Generates new rows in worksheet based on user input and pre-determined 
    parameters for what documents are associated with a role.
    """
    while True:
        print(f"Please enter new user name:\n")
        new_fname = input("First name \n")
        new_lname = input("Last name \n")
        
        if validate_name_input(new_fname, new_lname):
            break

    new_role = input_role()
    new_date = input_new_date()
    deadline_date = calc_deadline(new_date)

    first_new_row = []
    first_new_row.extend((new_fname, new_lname, new_role, deadline_date, "Planned"))
    second_new_row = first_new_row.copy()
    third_new_row = first_new_row.copy()
    first_new_row.append("CV")
    second_new_row.append("GCP Certificate")

    if new_role == "1" or new_role == "2":
        third_new_row.append("Financial Disclosure")
    elif new_role == "3":
        third_new_row.append("IATA Certificate")

    all_new_rows = [first_new_row, second_new_row, third_new_row]
    print(f"Following rows are added to worksheet {all_new_rows}")
    return all_new_rows


def input_new_date():
    """
    Request user to provide start date in specific format. 
    Uses a while loop to keep running until input is valid. Calls validation function
    for date input.
    Returns the date string provided.
    """
    while True:
        print(f"Please enter start date:\n")
        print(f"Use date format YYYY-MM-DD:\n")
        print(f"Example 2021-10-07:\n")
        new_date = input("Date \n")

        if validate_date_input(new_date) and validate_time_delta(new_date):
            print("Thank you for providing date!")
            break
        
    return new_date


def calc_deadline(date):
    """
    Converts user input date string to datetime using strptime method
    Calculates new deadline 15 days ahead using timedelta and returns the
    calculated deadline date converted back to a string.
    """
    date_time_str = date
    date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d')
    deadline_date = date_time_obj + timedelta(15)
    deadline_date_string = deadline_date.strftime("%Y-%m-%d")
    print(f"Your new deadline for follow up is {deadline_date_string}")
    return deadline_date_string


def add_doc_rows(data, worksheet):
    """
    Receives a list of lists with staff data to be inserted into a worksheet
    Updates the relevant worksheet with the data provided and prints out statement
    to user with action taken and completed.
    """
    print(f"Adding staff and documents to {worksheet} worksheet...\n")
    for row in data:
        worksheet_to_update = SHEET.worksheet(worksheet)
        worksheet_to_update.append_row(row)
    print(f"{worksheet} worksheet updated!\n")


def request_update_by():
    """
    Requests the user to choose a filter from role, deadline and all.
    Calls function to validate the user input based on numbered options.
    Uses a while loop to keep running until input is valid.
    Returns variable update_filter with the chosen action
    """
    while True:

        print("Please chose filter:\n")
        print("1 : Role         Returns list filtered by selected role")
        print("2 : Deadline     Returns list filtered by approaching deadline")
        print("3 : All          Returns full list of rows in Document Tracking\n")
        options = ["1", "2", "3"]
        update_filter = input("Filter: \n")

        if validate_user_input(update_filter, options):
            break
    return update_filter


def request_update_role():
    """
    Requests the user to choose what role to update.
    Calls function to validate the user input based on numbered options.
    Uses a while loop to keep running until input is valid.
    Returns variable update_role.
    """
    while True:

        print("Please select role to update:\n")
        print("1 : PI       Principal Investigator")
        print("2 : Sub-I    Sub-Investigator")
        print("3 : SC       Study Coordinator\n")
        options = ["1", "2", "3"]
        update_role = input("Role: \n")

        if validate_user_input(update_role, options):
            break
    
    print(f"You picked {update_role}")
    return update_role


def update_status_input():

    """
    Requests the user to choose an updates document status from options.
    Calls function to validate the user input based on numbered options.
    Uses a while loop to keep running until input is valid.
    Converts the numbered choice to a string and returns variable new_status 
    with the string generated.
    """

    while True:
        print("\nPlease indicate new document status:")
        print("Document default status is 'Planned':\n")
        print("1 : Sent         Document template has been sent")
        print("2 : Requested    Document has been requested")
        print("3 : Complete     Completed document has been recevied \n")
        new_status = input("New status: \n")
        options = ["1", "2", "3"]

        if validate_user_input(new_status, options):
            print("Thank you!")
            break
    
    if new_status == "1":
        new_status = "Sent"
    elif new_status == "2":
        new_status = "Requested"
    elif new_status == "3":
        new_status = "Complete"

    return new_status


def print_list_role():
    """
    Calls and uses return values from request_update_role function and
    add_row_numbers function.
    Filters the list based on user choice and prints the list to the terminal.
    
    """
    all_rows = add_row_number()
    update_role = request_update_role()
    print(update_role)
    if update_role == "3":
        filtered_list_sc = list(filter(lambda x: "SC" in x, all_rows))
        for row in filtered_list_sc:
            print(*row)   
        return filtered_list_sc
    elif update_role == "1":
        filtered_list_pi = list(filter(lambda x: "PI" in x, all_rows))
        for row in filtered_list_pi:
            print(*row)
        return filtered_list_pi
    elif update_role == "2":
        filtered_list_subi = list(filter(lambda x: "Sub-I" in x, all_rows))
        for row in filtered_list_subi:
            print(*row)
        return filtered_list_subi
    

def print_list_deadline():
    """
    Creates a new list of date strings from the worksheet and converts string into dates
    Calculates the date difference from deadline to today and returns new list
    of difference in days.
    Appends the date difference in days back to the full list and prints list
    sorted by days to deadline to the terminal.
    """
    all_rows = add_row_number()
    date_list = []
    for row in all_rows[1:]:
        date_list.append(row[4])
   
    converted_date_list = [datetime.datetime.strptime(date, '%Y-%m-%d').date() for date in date_list]
    diff_days = []
    today = datetime.date.today()
    for date in converted_date_list:
        diff = date - today
        diff_days.append(diff.days)
    
    i = 0
    for row in all_rows[1:]:
        row.append(diff_days[i])
        i = i + 1

    sorted_rows = sorted(all_rows[1:], key=lambda x: x[7])
    for row in sorted_rows:
            print(*row) 
     

def add_row_number():
    """
    Pulls all rows from the doc collection worksheet.
    Iterates through the list of lists, appending an increasing row 
    number first in each list, returns a full list of lists with corresponding
    row numbers in the worksheet.
    """
    all_rows = SHEET.worksheet("doc_collection").get_all_values()
    index = 1
    for row in all_rows:
        row.insert(0, f"Row # {index}")
        index = index + 1
    return all_rows


def update_doc_status(worksheet):
    """
    Request user input on what row to update and calls function for new document status.
    Updates corresponding row and columns 4 and 5 with new status and new calculated deadline.
    """
    row_number = input("Row number:\n")   

    new_status = update_status_input()

    new_date = input_new_date()
    new_deadline = calc_deadline(new_date)
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.update_cell(row_number, 5, new_status)
    worksheet_to_update.update_cell(row_number, 4, new_deadline)
    print(f"{worksheet} worksheet updated with new document status!\n")


def print_all():
    all_rows = add_row_number()
    for row in all_rows:
            print(*row) 


def run_again_input():
    """
    Requests user to chose if they want to perform another action or stop running
    the application. 
    Calls function to validate that user input matched the given options.
    Uses a while loop to keep running until input is valid. Accepts uppercase and lowercase
    letters for Y/N. 
    """
    while True:
        print("Do you want to perform another action?\n")
        options = ["Y", "y", "N", "n"]
        answer = input("Y/N \n")

        if validate_user_input(answer, options):
            break
    
    print(f"You picked {answer}")
    return answer


def run_again():
    """
    Re-runs program if user wants to perform another task. 
    Closes program with a message if user does not want to perform another task.
    """
    answer = run_again_input()  

    if answer == "Y" or answer == "y":
        main()
    elif answer == "N" or answer == "n":
        print("Bye, thank you, come again")


def validate_name_input(fname, lname):
    """
    Validates first name and last name inputs. Names can be letters only
    and must be between 2 and 15 charachters each for first name and last name
    Generates error message for user to define the error made.
    """
    try:
        if fname.isalpha() and lname.isalpha():
            print("Fname and lname letters only")
        else:
            raise ValueError(
                "First name and last name must consist of letters only"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
        
    try:
        if (len(fname) >= 2 and len(fname) <= 15) and (len(lname) >= 2 and len(lname) <= 15):
            print("Corrent length")
        else:
            raise ValueError(
                "Name must be 2 - 15 characters long"
            )
    
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
       
    return True


def validate_date_input(date):
    """
    Validates time input. Converts input date string to date and by compares with 
    given format of YYYY-MM-DD. Raises error and error message if not provided correctly. 
    """

    try:
        if datetime.datetime.strptime(date, "%Y-%m-%d"):
            print("This is the correct date string format.")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def validate_user_input(user_input, options):
    """
    Validates user input from list of defined options. 
    Generates error message if user input does not match given options.
    """
    try:
        if user_input in options:
            print("Thank you!")
        else:
            raise ValueError(
                "You need to pick one of the given options"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def validate_time_delta(date):
    """
    Validates input dates. Raises error if date is in the future.
    Prints a note/warning if input date is more than 15 days in the past and deadline
    has already passed.
    """
    now = datetime.datetime.now()
    print ("Current date:")
    print (now.strftime("%Y-%m-%d"))
    new = datetime.datetime.strptime(date, "%Y-%m-%d")

    try:
        if new < now + timedelta(-15):
            print("Note! Date more than 15 days in past, deadline overdue")
        elif new > now:
            raise ValueError(
                "Date cannot be in the future"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def main():
    """
    Runs the program and functions depending on user
    choices and inputs
    """
    user_input = input_action()
    if user_input == "1":
        all_new_rows = create_rows()
        add_doc_rows(all_new_rows, "doc_collection")
    elif user_input == "2":
        update_filter = request_update_by()
        if update_filter == "1":
            print_list_role()
            update_doc_status("doc_collection")
        elif update_filter == "2":
            print_list_deadline()
            update_doc_status("doc_collection")
        elif update_filter == "3":
            print_all()
            update_doc_status("doc_collection")           
    elif user_input == "3":
        print("Printed status here")
        print_all()
    run_again()

        
print("Welcome to Document Status Tracking!")    
main()

