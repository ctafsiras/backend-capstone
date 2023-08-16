# Description
This repo for my final backend specialisation provided by Meta 

# Project setup 
1. You need  to install python, if you dont have it installed already
2. You need  to setup your virtual enviroment, in case for this project we use `pipenv shell` command to create or activate virtual enviroment and it will create  `Pipfile` which contained all neccessary setup such as version of python you are using.
3. you have to create project using `django-admin startproject backend_capstone` command here in the backend_capestone is the project name and create app with this command  `django-admin startapp backend_capestone_app` here backend_capestone_app is the nae of the app.
4. you need to install django using `pipenv install django` command
5. you need to install django using `pipenv install djangorestframework` command

# setup for mysql
1. You ve to download and install mysql , if you dont have it installed already once you are done, then run the following command to `sudo mysql -u root -p` or simply remove the sudo and run the command for Window os.
2. by default mysql has password "" then click enter
3. then you have to create new database using the following command `create database backenddb;` once you run the command.
4. then create user if you are not a root user with the following command `CREATE USER 'adminbackend'@'localhost' IDENTIFIED BY 'backend@123';` and grant all previledges to the user and run flush previledges. Below is the screen short of the mysql setup.
![Screenshot_2023-08-07_10_29_24](https://github.com/alaminthespecial/backend_capstone/assets/82694244/1ba04843-91e3-4065-999c-3e1ca526ea4b)
