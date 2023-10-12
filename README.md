Note" Changes made after the deadline are only made to the readme file

Karanc Project Description:
-----------------------

Description:
------------
Karanc is a microagent communication project that leverages the uagents library from fetch.ai. It serves as a practical tool for traders and individuals who regularly engage in currency conversion tasks. The solution offers users the ability to specify the base currency, the foreign currency, and set minimum and maximum limits to trigger alerts.

Getting Started:
---------------
To run this project on your machine, follow these steps:

Clone the repository to your local machine:


Project Structure:
------------------
This repository includes two main folders:

Console-based Microagent Communication (Microagents):

Demonstrates microagent communication through a console-based interface.
Web-based Implementation:

Showcases the web-based implementation of the Karanc Project.

Setup:
----------
To run this project, you'll need to install the following libraries:

uagents
requests
json

Currency Exchange API
------------------------
For currency exchange data, you'll need to generate an API URL from [Exchange Rate Api]('https://exchangeratesapi.io/').

WhatsApp Notifications
---------------------
To enable WhatsApp notifications, send the message "I allow callmebot to send me messages" to [+34644718199]('https://wa.me/+34644718199').


Instructions for Microagent Communication
------------------------------------------
To see microagent communication in action:

You need to add api keys of Call me Bot and Exchange rate api to .env file.

.env file
```
WHATSAPP_API_KEY = {ENTER THE api key acquired in the whatsapp message}
EXCHANGE_RATE_API_KEY = {Enter the exchange rate api key}
```
Navigate to the "agents" folder.
Inside this folder, run the "agent.py" and "user.py" files.
```python agent.py to run agent file run this in the terminal```
```python user.py to give the base currency, foreign currency and minnimum and maximum limit run the file. The two files are needed to run in terminal separately```

Provide the required input in the "user.py" file console.

Instructions for Web-Based Implementation:
-----------------------------------------
To experience the web-based functionality, do the following:

Enter the "Karanc" folder.
Run the below command
```
python manage.py runserver
```

Go  to [web app]('127.0.0.1/8000/Karanc')
You will be redirected to a functioning web page, where you can explore the project's web-based features.
Go to [Youtube Videos]('https://youtu.be/vRRdwliWz-s?si=k5YvZV7KxoBQP5Am')
to see the handon project.

