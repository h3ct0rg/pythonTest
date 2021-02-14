# pythonTest

Repository to handle the code from a technical test to develop the backend and rest api endpoints to handle information of items

# Branchs

* Master:
	- initial state
* Develop:
	- Solution Code
	
# Steps to initialize environment

1) Start virtual environment.
	* move inside the folder: solution/env/scripts/
	* run the command "activate"

2) Install dependencies.
	* move inside the folder: solution/env/requirements/
	* then run the command "pip install -r local.txt"

3) run the migration.
	* move to the main folder solution that contains manage.py
	* generate the migration: "python manage.py makemigrations"
	* run the migration: "python manage.py migrate"
	* crate the superuser: "python manage.py createsuperuser"
	* start the server: "python manage.py runserver --settings=solution.settings.local"
	
#solve swagger know issue
It's a bug in the developer's code, 
in site-packages/rest_framework_swagger/templates/rest_framework_swagger/index.html
The line with {% load staticfiles %} (line 2) should be {% load static %}. 
Edit it manually