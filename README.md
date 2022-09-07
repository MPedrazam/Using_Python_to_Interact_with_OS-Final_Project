# Using-Python-to-Interact-with-the-Operating-System---Final-Project
Final project in the course Using Python to Interact with the Operating System, from the Google IT Automation with Python Professional Certificate.
https://www.coursera.org/learn/python-operating-system/gradedLti/x0cNf/qwiklabs-assessment-log-analysis-using-regular-expressions

The aim of these project is to create a script, named ticky_check.py, that generates two different reports based on the ranking of errors generated by the system and the user usage statistics for the service i.e., syslog.log. This script create the following reports:

- The ranking of errors generated by the system: A list of all the error messages logged and how many times each error was found, sorted by the most common error to the least common error. This report doesn't take into account the users involved.
- The user usage statistics for the service: A list of all users that have used the system, including how many info messages and how many error messages they've generated. This report is sorted by username.

In the development of these scipt, it was used regex laguage to parse a log file, appended and modified values in a dictionary and wrote to a file in CSV format.
