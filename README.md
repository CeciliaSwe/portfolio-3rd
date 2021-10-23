# Ultimate Document Tracking

## Intro

Document tracking is a Python Terminal application which runs in the Code Institute mock terminal on Heroku.

The application is intended for Document tracking for various site staff roles within Pharmaceutical Clinical Trials and can be used to facilitate document tracking in gspread by adding rows applicable for the given input.

The live site can be found [here](https://portfolio-3rd.herokuapp.com/)


## Design

### Application Workflow
Below is a high level overview of the workflow through the application.

![Code Logic Flow Chart](assets/images/flowchart-p3.png)

### User Stories
-  __As a user of the application, I want to be able to:__
    - Add new site staff and have applicable documents with corresponding rows added to my gspread worksheet.
    - Get the follow up deadline calculated and presented to me.
    - Update existing rows woth a new status and have a new deadline calculated and presented to me.
    - Have an intuitive UI that makes it clear what operations I can perform and what input is expected from me.
    - Make chioices and enter input quickly, without having to type more than neccesary.
    - Have available data presented to me.


### Audience
The intended audience is anyone working with spreadsheet document tracking in clinical trials and would benefit from an automated process of adding and updating the sheet.

## Features

### Existing features
- Generate new rows in worksheet - "New"

- Update status and date of existing rows in worksheet
- Print tabular views of all documents currently in worksheet

- Accepts user input
    - Numbered options where there are multiple, fixed choices
    - Any letters of certain lengths for first- and last names
    - Date in specified format
    - Yes / No option

- Generates future deadline for next follow up
- Input validation and error checking:
    - Numbered options: You can only enter the numbers specified as options. No out of range numbers, letter or symbols are accepted.
    - First- and last names: You must enter letters only and 2-15 characters for first- and last names respectively.
    - Dates: Must be entered in specified format YYYY-MM-DD, no alternative format is accepted.
    - Yes/No: Must be entered

### Future Features

## Testing

###
# Testing
## User Story Testing
-  __User Features Requested:__
    - Request: Add new site staff and have applicable documents with corresponding rows added to my gspread worksheet.
        - Result: The user can choose the option "New", enter the new site staff data (name, role and start date) and have their worksheet upated with corresponding rows for each required document.
    - Request: Get the follow up deadline calculated and presented to me.
        - Result: The application automatically returns a deadline calculated as the start date plus 15 days. It is printed tp the terminal and added to each new row in the worksheet.
    - Request: Update existing rows woth a new status and have a new deadline calculated and presented to me.
        - Result: The user can choose the option "Update", filter by role, by deadline or see all existing rows in the worksheet, and update the status of a chosen row. A new deadline will automatically be calculated and presented.
    - Request: Have an intuitive UI that makes it clear what operations I can perform and what input is expected from me.
        - Result: The application has a clear menu and user prompts, presenting each option (where applicable) with a short explanation. Abbreviations which are not immediately clear are explained.
    - Request: Make choices and enter input quickly, without having to type more than neccesary.
        - Result: The application uses numbered options where possible to reduce the amount of typing for the user.
    - Request: Have available data presented to me.
        - Result: The user can choose the option "Status" which prints a tabulated data to the terminal, giving an overview of the available data from the worksheet. The option "Update" also prints tabulated data based on user's preferred filter.


## Data model

## Technologies

### Languages

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Other Technologies and Libraries

- [GitHub](https://github.com/)
- [Git](https://gitforwindows.org/)
- [Heroku](https://heroku.com)
- [Lucidcharts](https://www.lucidchart.com/)

## Bugs & Fixes


- Calculated deadline could not be inserted in worksheet, solved by converting the date back to string format before insertion (https://github.com/burnash/gspread/issues/511)

## Testing

### [TESTING SHEET]()

### User testing feedback.

## Deployment

### Creating App

1. To import the required dependencies to the requirements.txt file, type the following in the terminal:
    > pip3 freeze > requirements.txt
    - Heroku will use this file to import the dependencies that are required.
2. Log into or sign up to Heroku.
3. On the dashboard, select "Create new app" from the drop-down menu (upper right corner) or the button mid-page.
6. Provide a name for your application (this needs to be unique) and select your region.
7. Click "Create App".

### Update settings

1. Navigate to "Settings" and scroll down to "config vars".
2. For the first row: for key: type "CREDS" and for value: copy and paste the content of the creds.json file. Click "add".
3. For the second row in config vars: for key: type "PORT" and for value type: "8000". Click add.
4. Scroll down to "build packs".
5. Click "build packs" and then add both "python" and "node.js" - in that particular order.


### App Deployment

1. Navigate to the "Deploy" section.
2. Scroll down to "Deployment Method" and select "GitHub".
3. Authorize the connection of Heroku to GitHub.
4. Search for your GitHub repository name (portfolio-3rd), and select the repository.
5. For Deployment there are two options, Automatic Deployments or Manual.
    - Automatic Deployment: This will prompt Heroku to re-build your app each time you push your code to GitHub.
    - Manual Deployment: This will only prompt Heroku to build your app when you manually tell it to do so.
6. Ensure the correct branch is selected "master/Main", and select the deployment method that you desire. In this case, I will be using Automatic Deployment.

## Credits

[Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template)


