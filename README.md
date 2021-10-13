# Portfolio 3

## Intro

The live site can be found [here](https://portfolio-3rd.herokuapp.com/)


## Design

![Code Logic Flow Chart](assets/images/flowchart-p3.png)


### Goals

### Audience

## Features
### Existing features
### Future Features

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


