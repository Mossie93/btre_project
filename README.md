# BT Real Estate

:warning: **Work in Progress** :warning:

A real estate web application developed as part of Python & Django tutorial from Udemy.

## Requirements

- Python 3
- Django 3.0.5
- PostgreSQL 11

## Setup

Run the steps below in order to set up the project and run local Django server:

1. On your local machine, set the following env variables:
```
export BTRE_DB_NAME="some_value"
export BTRE_DB_USER="some_value"
export BTRE_DB_PASSWORD="some_value"
export BTRE_DB_HOST="some_value"
```
*Please remember to replace some_value stringss above with the values of your choice.*

2. Run the following commands:
```
pip3 install -r requirements.txt
ppython3 manage.py migrates
python3 manage.py runserver
```

## Testing

TBD