# Base API for Political Sentiment and Community Analysis

## Install Django if you don't have it already (_globally_)

``pip install django``

## Run the project

``python manage.py runserver``

> you might need to use **python3** instead of **python**


## Architectural Details

### Controllers

- receive the requests and send them over to the services and sends back the responses
- contain separate methods for each HTTP verbs (most used: GET, DELETE, POST, PUT, PATCH)

### Services

- there will be the bussiness logic

### Repositories

- they communicate with the the database to perform CRUD operations (**NO** bussiness logic there!)

### Middleware

- intercepts requests and checks the JWT Token for authentication/authorization

### Models

- classes that describe database tables