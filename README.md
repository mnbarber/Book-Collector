# Django Project

## Startup Project

- create your project folder and cd into it(mine is book_collector_app)
- setup django environment
    - pip3 install pipenv
    - pipenv install django
    - pipenv shell
- run the django start command to setup project folders
    - django-admin startproject <projectname> . 
- generate starting app
    - django-admin startapp main_app
- navigate to projectfolder/settings.py, scroll to INSTALLED_APPS and add 'main_app' to the bottom, then in DATABASES insert <projectname> after 'NAME' and change the line above to say 'postgresql' at the end of the line instead of the sqlite part
- in terminal, pip3 install psycopg2-binary
    - then createdb <projectname>
    - then python3 manage.py migrate
- in terminal, python3 manage.py runserver
- everything should be running if you go to localhost:8000, now we can do stuff!