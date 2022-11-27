# FRISS Coding Assignment

## Summary

We want you to create 2 endpoints:
- Receives and stores a person
- Calculates the probability that 2 persons are the same physical person.

A person is represented by the following attributes:
- First name
- Last name
- Date of birth (can be unknown)
- Identification number (can be unknown)

The matching logic should work in the following way:
- If the Identification number matches then 100%


## Project structure


- `sql_app`: contains files db.py, which is for integrating database with our application.
models.py, which is for creating database model, Person.
repositories.py that contains some reusable functions to interact with the data in the database. schemas.py will contain the Pydantic models for our SQLAlchemy models.

- `fraud_detection`: in this project, I implemented the strategy for checking fraud by using strategy design pattern. Although at this moment there is only one strategy for checking fraud, we can easily add more strategies or modify the existing ones.

## Installation

Verify the python version installed. This project was built using python 3.7
```
python --version
```

Activate the virtualenv
```
pipenv shell --python 3.7
```

Install project dependencies requirement.txt
```
pip3 install -r requirements.txt

## Usage

To run the app localy, go to the root directory and run
```
uvicorn main:app --reload
```

you can visit http://localhost:8000/docs to see your API docs.

## Tests

To run units and integration tests move in the root directory and run:

```
pytest


## Docker

To run the app in docker, go to the root directory and simply run:

```
docker-compose up
```
