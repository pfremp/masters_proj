# Participant Finder Django Application
This application enables researchers looking for human participants to sign up and post their experiments. Participants are then able to register and sign up for experiments.
# Setup Application 

Steps to get application working

1. Create new Virtual Env: 
    ```
    mkvirtualenv partfinder
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
   ```
   ./manage.py syncdb
   ```
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
Setup Django All Auth in order to use Google Social Authentication.

### Site Name
Firstly, set the site name from the from the default 'example.com' to the partfinder details (this is essential for Django All Auth).

 - Click on 'sites' in the main admin area.
 - Select 'example.com'.
 - Enter your localhost URL as the Domain Name (e.g. http://127.0.0.1:8000) and part_finder.com for the 'Display Name'.

From the main admin area select 'Social Applications' then 'Add social application'. Enter the credentials below. 
### Localhost Credentials:
 - Provider: ```Google```
 - Name: ```Google```
 - Client ID: 
     ```
     448376006900-qatchgenmro1u9vbah2heqqq87ur8vgv.apps.googleusercontent.com
    ```
 - Secret:
    ```
    wMpbW4grIc3aXiyjqebetx7M
    ```
 - Leave 'key' blank.
 - Add site and then save.

##### Additional Info:
 - URI:
    ```
    http://127.0.0.1:8000/accounts/google/login/callback/
    ```
 - JS:
    ```
    http://localhost:8000/
    ```
The website should now be working and be able to be viewed at your localhost URL.

##### The locations of the preloaded experiments need to be manually configured via the django admin area. They will currently show as “None”.
##
##
#### Demo Researcher
 - Username: ```fsmith```
 - Password: ```111111```

### Demo Participant
 - Username: ```andrews1``` 
 - Password: ```111111```

## Video Demo
A video demo exhibiting the main features of the application can be viewed here: https://youtu.be/9Z7l5_THo8s

