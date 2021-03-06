# Books sharing REST API

This is my Flask pet project in frames of Python Web Programming course in CursorIt.School.
"Books sharing" API is a backend part of the application the main task of which is interaction between database(next is db) and client via sending and recieving JSON-formatted objects. Users are able to add books to the db, share those with other users via either direct application or email. Extras include posibilites to hide books, create wish lists and own libraries.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisites

You should have at least Python version 3.6 and PostgresSQL database installed on your local machine to be able to use this application. All dependencies are listed in **requirements.txt** To install the latter simply enter in either terminal or a prompt the following command:

```
pip install -r requirements.txt

```

## Installing

Clone this repo onto your local machine by the following command:

### https
```
git clone https://github.com/AleksMD/books_sharing.git

```
Create .env file in the root directory of the project.
Add environment variables and settings to the .env file:

```
PG_USER='your_postgres_user'
PG_PASSWORD='your_postgres_password'
PG_HOST='localhost'
PG_PORT=5432
PG_DATABASE='test_bookshare'
MAIL_USERNAME='your_username'
MAIL_PASSWORD='your_password'
MAIL_SERVER='smtp.gmail.com' // or any other
MAIL_PORT=465 // or any other
```
N.B. Database in postgres should be created before you start running the application.
To do so, open postgres db in terminal by this command:

```
sudo -u postgres psql
```
In opened terminal window enter:

```
CREATE DATABASE name_of_your_app_database;

```

Create user in postgres:

```
CREATE USER your_user_name WITH PASSWORD 'your_password';

```

Grant access to the database to the user:
```
GRANT ALL PRIVILEGES ON DATABASE name_of_your_app_database TO your_user_name;
```

After database was created and all variables was added to .env file you are ready to start.
To start the app run following command in terminal in root directory of the project:
```
python3 manage.py runserver

```
In the root page of the localhost - 127.0.0.1:5000/ (port 5000 is a default).
If the start of this app was succussfull you see map of main endpoints of API. It looks like something like the below:

```
{
  "endpoints": [
    {
      "resource": {
        "url": "/books",
        "description": "Returns either list of all books in the database (except hidden) or particular book if requested"
      }
    },
    {
      "resource": {
        "url": "/books/add_new_book",
        "description": "Add new book to the database (except hidden)"
      }
    },
# and many more...
```
it means that everything works fine.

See next section to understand how you can test this app.

## Running the tests
There are lots of test cases for this application.
To run all of those use following command:

```
python -m manage runtests

```

## Deployment

In order to deploy application on either local machine or virtual box run the following command in a command prompt:

```
docker-compose up

```
N.B. Either your local machine or virtual machine must contain docker and postgres on board.

In order to connect to the PostgresSQL in another docker container instead of the local machine you have to customize
docker-compose file in a way like the following:
```
version: '3'

volumes:
  database_data:
    driver: local

services:
  db:
    build: ./db
    ports:
        - 5432:5432
    volumes:
      - database_data:/var/lib/postgresql/data

  api:
    build: .
    ports:
      - 8000:8000
    volumes:
      - ./api:/usr/src/app/
    links:
      - db
    environment:
      - PG_HOST=db
      - PG_DATABASE=postgres_test_db
      - PG_USER=postgres_test_user
      - PG_PASSWORD=any_password_you_know
      - PG_PORT=5432
    command: "python manage.py runserver --host=0.0.0.0 --port=8000"
    depends_on:
        - db
``` 
### Be Aware
That if on your local machine PostgresSQL has been already installed you have two options to avoid conccurrency between two instances of Postgres that are both listening port 5432.
The first one is temporarely disable PostgresSQL on your local machine by the following command:
```
sudo systemctl stop postgresql # use 'restart' instead of 'stop' to revert                                # it back
```
The second one is simply change ports for db in 'docker-compose.yml' file:
```
db:
    ...
    ports:
    -5433:5433
    ...
api:
    ...
    environment:
    ...
    - PG_PORT=5433
    ...
```
## Built With

* [Python3.7](https://www.python.org) - The programming language of the app
* [Flask-Restful](https://maven.apache.org/) - The web framework used
* [PostgresSQL](https://rometools.github.io/rome/) - The relational database used
* [SQLAlchemy](https://www.sqlalchemy.org) - The ORM used

## Versioning

Version 0.0.1

## Authors

* **Oleksandr Budonniy** - *Initial work* - [AleksMD](https://github.com/AleksMD)

## License

Under no license

## Acknowledgments

* Thanks to the staff of CursorEducation.ITSchool especially to Python course team. Guys you are awesome teachers! 

