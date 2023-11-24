# comp3005A4

Dominic Rochon
3005 Assignment 4

Databse Setup Instructions:

Create a database named "students". This can be done by logging into pgAdmin4, selecting or creating a server, and creating a new database named "students". 
Make sure that your server's port number is "5432", that the hostname is "localhost", and that the username is "postgres". These can all be viewed by clikcing a server and looking under "Properties". To edit these values, press the pencil button and edit the parameters under the "Connection" tab.


Running the Program:

The program can be run by going to the program's location in cmd and typing "python 3005Assignment4Q1.py"
The program will ask you to enter the password to your server, after which you will be able to use commands on the database until the user quits.


Explanation of functions:

setup: This function drops every table from the database and then creates the student table and inserts the different students into that table. Essentially this starts the database from scratch.
getAllStudents: This function returns all the students in the database
addStudent: This function inserts a student into the database, with parameters of all required information
updateStudentEmail: This function updates the email of a student with a specific ID
deleteStudent: This function deletes a student with the inputted ID
main(): Driver function for testing all the other functions.


https://youtu.be/ZsPp0TKfU9s
