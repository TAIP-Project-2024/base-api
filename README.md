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

- there will be the business logic

### Repositories

- they communicate with the database to perform CRUD operations (**NO** business logic there!)

### Middleware

- intercepts requests and checks the JWT Token for authentication/authorization

### Models

- classes that describe database tables


---

Example of a project structure:

```
api
	controllers
		general
		ml
		sentiment
		topics
		community
	db
	factories
	middleware
	migrations
	ml_core
		data_preprocessing
		evaluation
		models
		sentiment_analysis
		topic_modeling
		community_detection
		utils
	visualizations
		sentiment
		topics
		community
	config
models
	domain
	lib
	ml
repositories
	general
	sentiment
	topics
	community
services
	general
	layouts
	sentiment
	topics
	community
BaseAPI
resources
```