# Air-Traffic-Control-System

You will require MySQL to be installed on the system and will also need to change the parameters in line 14 to access your mysql server.

All the listed files are required for proper functioning of the application, Do NOT remove any of the files.

ATC.py- Main program file that handles SQL connectivity.

Create.py- Contains modules required for creation, insertion and deletion within the database.

FLNO_generator.py- Contains module to populate the aiport with randomly generated 5-digit flight numbers.

Landing.py- Contains module that manages the process of the plane landing and adds it to the queue of planes waiting to be assigned a runway.

Timetaken.py- Contains module that retrieves the amount of time taken for the plane to move from one point to another in the airport from the table in MySQL.

cap_check.py- Contains modules to check if 1. There are free spaces in locations to move planes to and 2. There are any planes present in a location that can be moved to another location.

display.py- Contains module that returns a list of flights at a location.

ex_handler.py- Contains module that deals with exception handling making sure that the input is present in the list provided as one of the parameters. Best used for yes/no situations.

main_menu.py- Contains the main program that deals with the menu based interface.

rw_assign.py- Contains module responsible for the assignment and movement of flights from terminals to runways

takeoff.py- Contains module that manages the process of the plane taking off and removes it to the queue of planes waiting to leave.

term_assign.py- Contains module responsible for the assignment and movement of flights from runways to terminals after landing.


Additional packages required:
MySQLConnector
