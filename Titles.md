- Django mvt
- Django managment tool (django-admin)
- urls.py
- async or syncronouse
- what is app
- _django-admin startapp_
- mostly the main requirment of a app is user
- modules in a app directory
- migration folder for additional models
- apps can contain some subapps
- user models
    - extending the existing User
    - using AbstractUser in auth.model
- adding app to INSTALLED_APPS in setting.py
- adding AUTH_USER_MODEL = 'user.MyUser' to setting.py
- sqlite
- adding all models with makemigrations command (_django-admin makemigrations_)
- app>migration>0001_initial.py
- _django-admin migrate_
- _django-admin createsuperuser_
- unique = True
- _django-admin runserver_

- pipenv