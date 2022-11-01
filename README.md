# SIMPLE PRODUCT APIs

This is a simple backend application that uploads data from a `.json` file to the database and creates simple queries such as:
- get all products query
- get a single product query

## Technologies Used

The technologies used in this project are:

- Django
- GraphQL-Graphene
- SQLite3
- Docker
## Installation

Clone this repository on your local machine by using the `git clone` command

> **Requirements**: Docker. If you're unsure of having docker on your local machine, run `docker --version` on your terminal

### Build Docker Image

- Run `docker-compose build` to build the necessary docker images and install necessary dependencies

### Start the Project

- Run `docker-compose up` to start the project

### GraphQL Playground

-  Go to the browser and run `localhost:8000/graphql/` to access the graphql playground in order to test out the queries found in the `/product/queries.py` file
