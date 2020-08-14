# CSV_Uploader

Steps To Follow To Run this Project.

1. Copy repository link and clone project.
#git clone <project repo link>
or
Downlown Zip file

2.Change Postgres configuration as per your setup in settings.py.
#CSV_Django_Task -> settings.py -> DATABASES -> change Name = "AnyDbName or create csv name db", USER = 'Username', Pass = "Pass".
 or 
Install Postgressql 

* sudo apt-get install postgresql postgresql-contrib


After configuring db and settings

3. Run command in project Directory where manage.py file located.
#python manage.py makemigrations
#python manage.py migrate

After Successfully of migrations

RUN

#python manage.py runserver

4.Go to browser and type in URL
#http://127.0.0.1:8000/

5.Download CSV File format to test.


Thank You



