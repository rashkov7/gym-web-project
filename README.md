# Project: ProGymCorner
## [-> Open the web project here <-](https://gym-corner.herokuapp.com/)
## Description:
It's small web project, designed as a Sport's page. Users/Custemers could share their experience, recipes and could find and sign for workouts also. It's available anly for registred users. The site has admins and different levels of perrmissions. Each registred user has a profile and favorites colections with recipes. 
### Used technologies.
 - Code language is Python3,
 - IDE - Pycharm
 - Python Framework Django
 - Python REST API will be included very soon
 - Asynchronous Tasks with Django and Celery,
 - Redis - broker server,
 - SQL DB with PostgreSQL database(on production) and sqldb(on DEBUG)
 - Docker - docker containers are used for Posgres, Redis, 
 - OOP/SOLID Principles were strictly observe.
 - HTML/CSS - front-end and a little bit JS.
  
## Some screenshopts:
<img src="https://res.cloudinary.com/dpe5acysn/image/upload/v1650232393/screenshots/pic_2_txjcsv.jpg" alt="landing page" style="height: 300px; width:500px;"/>
<img src="https://res.cloudinary.com/dpe5acysn/image/upload/v1650232488/screenshots/pic_3_vmhygv.jpg" alt="landing page" style="height: 300px; width:500px;"/>

##  How to Install and Run the Project
 - clone repository on your local machine
 - Create virtual environments in the project foolder
  ```python
     install python3-venv
     $ mkdir djangoenv. ...
     $ python3 -m venv djangoenv. ...
     Activate Virtual Environment.
 ```
 - Configure a Python interpreter
 - INSTALL requirements.txt wich is in the project
 ```python
    pip install -r requierements.txt
 ```
 - Run your broker server. redis-server.
 - Next run your Django server. python manage.py runserver
 - Next step run your Celery worker.
 - next run your scheduler.

## License 
License is free license software. 
