# Gym-Management-System-In-Django

Step 1: VIRTUAL ENVIRONMENT
        -> Create and activate virtual environment.
        -> Command: pipenv shell

Step 2: INSTALL DEPENDENCIES
        -> Install all the dependencies in the virtual environment.
        -> Command: pipenv install -r requirements.txt

Step 3: DATABASE MIGRATIONS
        -> Convert Model into Database through migrations.
        -> Command1: python manage.py makemigrations
        -> Command2: python manage.py migrate
        
Step 4: ADMIN CREDENTIALS
        -> Create an admin to manage your admin panel.
        -> Command: python manage.py createsuperuser
        -> Enter username and password to create admin.
        
        
 Step 5: SERVER 
         -> Run server locally to develop or view the project in action.
         -> Command: python manage.py runserver
         
