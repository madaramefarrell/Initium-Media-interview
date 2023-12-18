# Pre work for Initium Media Interview

## Description
Create a registration/login page using Docker + Nginx + Django.
Bonus Points: Implement employee status for Django admin site. Display "Employee" upon successful login if the user is an employee.
After completion, upload the project to git (any platform) and provide a downloadable link. Include a README file explaining how to run the entire service locally.

## Environment 
* macOS Sonoma 14.2 (23C64)
* Docker version 24.0.6, build ed223bc 
* Docker Compose version 2.23.3
* Django 4.2.8
* nginx:latest
* Python:latest
* Postgresql 14 

## Start local server
- Copy Settings File

    `cp ./InitiumMediaInterview/settings.py.default ./InitiumMediaInterview/settings.py`

- build image

    `docker-compose build`

- Start Container Services

    `docker-compose up -d`

- Go to home page

    Open browser and type `http://localhost` into the URL

- Go to login page

    Open browser and type `http://localhost/login/` into the URL

- Go to signup page

    Open browser and type `http://localhost/signup/` into the URL

- Open django admin site

    Open browser and type `http://localhost/admin` into the URL

- Stop and remove container services, and remove volume (volume for postgreSQL service)

    `docker-compose down -v`

## Router
- Home page

    `http://localhost/`

- Login page

    `http://localhost/login/`

- Signup page

    `http://localhost/signup/`

- Django admin site

    `http://localhost/admin/`
    

## Something about local server

Local include 3 users:

1. Superuser `root` with password `root`

2. Employee user `lily` with password `0000`

    ![lily](https://github.com/madaramefarrell/Initium-Media-interview/assets/5953450/b5e97b7d-ca27-4ff8-b222-b130adfe2857)

3. Not employee user `john` with password `0000`

   ![john](https://github.com/madaramefarrell/Initium-Media-interview/assets/5953450/3169df38-d5bb-484d-8502-ec8b72acc985)

    
