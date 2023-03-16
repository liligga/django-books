## Project Structure
This is a simple Django project. It contains the following directories:
- [Project Structure](#project-structure)
  - [Core](#core)
  - [Bookkeper](#bookkeper)
  - [Static](#static)
  - [Templates](#templates)
- [Usage](#usage)

### Core
This is main directory of the project with main settings, main `urls.py` file and so on 

### Bookkeper
This is the app directory that contains all models, views and other files related to `Books`

### Static
This is the directory with static files, such as css, javascript and static images

### Templates
This directory is solely for templates in this project

Models for database in this project are:
  - Book
    - title
    - publication_date
    - author
    - publisher
  - Author
    - name
    - email
  - Publisher
    - name
    - address

## Usage
To start this project on your machine 
  - clone the repository(`git clone https://github.com/liligga/django-books`)
  - create virtual environment(`python -m venv venv; source venv/bin/activate`)
  - install dependencies(`pip install -r requirements.txt`)
  - run migrations(`python manage.py migrate`)
  - create superuser(for admin panel)(`python manage.py createsuperuser`)
  - seed some data(`python manage.py seed`)
  - run server(`python manage.py runserver`)