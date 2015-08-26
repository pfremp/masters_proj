Steps to get app working:

1. Create new Virtual Env: virtualenv masters

2. Install requirements: pip install -r requirements.txt

3. Clone this repository

4. Make migrations: ./manage.py makemigrations

5. Sync Database: ./manage.py syncdb
	- Create Super User

6. Populate django cities light: ./manage.py cities_light or ./manage.py cities_light —force-all

7. Populate with population script: python populate_pf.py

8. Setup google authentication app:

a. Sign into the admin area
b. Select ‘Social Applications’
c. Select ‘Add new social application’

Localhost Credentials:
Client ID:448376006900-lfudj54u02f955pucnd4usp66epbgvd.apps.googleusercontent.com 
Secret:NqaB8QaEtnPsXAlIEjQ0C-H0 
Add website then save

Additional Info:
URI:http://127.0.0.1:8000/accounts/google/login/callback/
JS:http://localhost:8000/


pfremp1.pythonanywhere.com/part_finder credentials:
Client ID:448376006900-nlfudj54u02f955pucnd4usp66epbgvd.apps.googleusercontent.com
Secret:NqaB8QaEtnPsXAlIEjQ0C-H0

Additional Info:
URI:http://pfremp1.pythonanywhere.com/accounts/google/login/callback/

