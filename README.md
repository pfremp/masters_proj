# Participant Finder Django Application
This application enables researchers looking for human participants to sign up and post their experiments. Participants are then able to register and sign up for experiments.
# Setup Application 

Steps to get application working

1. Create new Virtual Env: 
    ```
    virtualenv partfinder
    ```
2. Clone this repository:
    ```
    git clone https://github.com/pfremp/masters_proj.git
    ```
3. Install requirements:
   ```
   pip install -r requirements.txt
   ```
4. Make migrations:
   ```
   ./manage.py makemigrations
   ```
5. Sync database (create Superuser)
6. Populate Django Cities Light:
    ```
    ./manage.py cities_light
    ```
    or
    ```
    ./manage.py cities_light —force-all
    ```
7. Populate DB with population script
    ```
    python populate_pf.py
    ```

# Setup Django All Auth
Setup Django All Auth in order to use Google Social Authentication
### Localhost Credentials:
 - Client ID: 
     ```
     448376006900-lfudj54u02f955pucnd4usp66epbgvd.apps.googleusercontent.com
    ```
 - Secret:
    ```
    NqaB8QaEtnPsXAlIEjQ0C-H0
    ```
Add website and then save

#### Additional Info:
 - URI:
    ```
    http://127.0.0.1:8000/accounts/google/login/callback/
    ```
 - JS:
    ```
    http://localhost:8000/
    ```
The website should now be working and be able to be viewed at your
localhost URL.

* The locations of the currently experiment need to be manually configured via the django admin area. They will currently show as “None”.

#### Demo Researcher
 - Username: fsmith 
 - Password: 111111
### Demo Participant
 - Username: andrews1 
 - Password: 111111

## Deployment
The web application is currently deployed on Python Anywhere and can be view at http://pfremp1.pythonanywhere.com/part_finder/.

PythonAnywhere Hosting Login:
 - https://www.pythonanywhere.com/login/
 - Username: pfremp1 
 - Password: pfmstrs1

Live Website Admin Credentials:
 - http://pfremp1.pythonanywhere.com/admin/
 - Username: Pfr1 
 - Password: pf1111



## Video Demo
A video demo exhibiting the main features of the application can be viewed here: https://youtu.be/9Z7l5_THo8s

