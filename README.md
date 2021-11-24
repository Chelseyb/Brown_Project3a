# Brown_Project3a
Project: Stock Data Visualization on the Web
Project Objectives
To extend the functionality of project 3 by making it accessible on the web.
To further gain experience and develop skill working with Docker and Flask.
To further develop team chemistry and communication skill.
Description
In this project you will extend the software application you developed in project 3 to be accessible on the web. You will achieve this using Docker and Flask. Docker provides the ability to package and run an application in a loosely isolated environment called a container. Docker is currently an industry-leading tool for developing containerized software applications. Flask is a lightweight WSGI web application framework that allows developers to create web applications using Python.

You will be provided with the Docker and Flask environment with a web form already working. You will have to add the relevant parts of the code you wrote for project 3 to complete the functionality of the web app to query the Alpha Vantage (Links to an external site.) api. You will also have to make one upgrade to the web app by adding code to populate the app with all the stock symbol options from the stock exchange.

Teams can, and are encouraged to, work on this project together but everyone will submit their work individually. This project does not have to be managed in Jira. The team should work together in helping each other to understand Docker, Flask, how to implement your code, and develop a solution to populate the stock options.

Purpose
The purpose of this project is to gain more knowledge and experience working in the Docker and Flask environments to produce a working software application.

Scenario
The professor you created the python application for loved it! He just wishes that he did not have to run it from the command line and that there was some sort of user interface. A teammate of yours suggests converting the app into a web app using Flask since the application is written in python. The app will also be deployed in a Docker container.

Your teammate went ahead and created the web form in Flask and inside a Docker container. You now have to add your python code to query the Alpha Vantage (Links to an external site.) api and display the chart in the browser to make the web app fully functional. You also have to write code to populate the stock symbols in the web app.

Project Tasks
Download the code  Download Download the codeand load the Flask app in Docker.
Add the code to query the api to the web app.
Write code to populate the stock symbol options in the web app.
What to submit
1. Download the Code and Load the Flask App in Docker
Beore you begin this step, make sure that Docker is running.

Download the zip file at the link provided above and extract the contents to a folder on your computer. Go into the “it-4320-project3a” folder and you will see the following files and folders:
docker-compose.yml
Dockerfile
config.py (Links to an external site.)
requirements.txt (Attention: Look at the contents of this file. If your scrum team used any python modules (like pandas) that are not listed in the file you should add those modules to the file before executing the command in step 2; one per line.)
wsgi.py (Links to an external site.)
LISENCE
flask_wtforms_tutorial (folder)
From your terminal (Mac) or command line (PC) go into “it-4320-project3a” folder and type the following command.
docker-compose up -d
The previous step would have run the docker-compose.yml and Dockerfile files to create the Docker container and Flask app. You can check to ensure that your container was created by looking at your Docker dashboard, or typing the following.
docker ps -a
You can view the application running in the web browser by going to the following url
http://0.0.0.0:5001/
To stop your container and application from running type the following command.
docker-compose down
2. Add Code to Query the Api
You are now ready to begin adding your code to the web app. The Flask app is running in debug mode which means when you make changes to the code on your computer the code on the app running inside your container also gets updated so you can view live code changes immediately without having to restart your container.

The functionality for the web app is implemented in three python files: charts.py,  routes.py, and forms.py files. You will add your code to the charts.py and routes.py files to query the api. The web app is structured in this way to implement Separation of Concerns (SoC), an important software engineering principle.

You should read through the following article on Separation of Concerns (SoC) (Links to an external site.)

Explanation of Files
charts.py will act as a library of python functions that are used to do the work of processing the form data and querying the api.
routes.py is where the logic to display the web page is implemented. This is where you will call the functions written in the charts.py file create the chart.
These files can be found in the flask_wtforms_tutorial folder.

3. Write Code to Populate the Stock Symbol Options
The forms.py file in the flask_wtforms_tutorial folder is where you will add your code to add the stock symbol options. You should not hard code the symbol options but rather, you should load them dynamically from somewhere: a file, a web resource, or somewhere else. You will see that the choices in the symbol field accepts a list of tuples.

Datahub.io (Links to an external site.) has a listing of json, csv, and other files types for download. Feel free to make use of other resources if you like.

What to Submit
Upload the project to a GitHub repository and submit the link when completed.
