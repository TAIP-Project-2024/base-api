## Install MongoDB if you don't have it already

``pip install pymongo[srv]``
``pip install python-dotenv``
- install extension MongoDB for VS CODE then restart Visual Studio Code

## Install PostgreSQL if you don't have it already

``pip install psycopg2``

## Install Bcrypt if you don't have it already

``pip install bcrypt``


## Summary of Design Patterns Used
### Dependency Injection Pattern:

- Used in ``ControllerUser`` to inject ``User``, ``ViewLogin``, and ``PostgresRepository`` dependencies.

### Repository Pattern:

- Implemented in both ``MongoRepository`` and ``PostgresRepository`` to abstract database operations. This helps in maintaining separation of concerns and makes testing easier.

### Factory Method Pattern:

- Implemented in the ``AnalysisFactory`` class to create instances of different analysis components based on the type requested. This promotes loose coupling between components.

### Data Transfer Object (DTO):

- The ``AnalysisResults`` class serves as a DTO to encapsulate and transfer data between layers.

### Single Responsibility Principle:

- Each class and method focuses on a single responsibility, enhancing maintainability and readability.

## Using AI (ChatGPT) to Solve Laboratory Tasks
### Implementation Overview
During the development of the project, I utilized ChatGPT as an AI assistant to assist with various coding tasks, including:
### Code Structure and Design Patterns:
I asked ChatGPT for guidance on implementing design patterns like the Repository Pattern and Factory Method, which helped me structure my code more effectively.
Error Handling and Best Practices:
ChatGPT provided insights on best practices for error handling and data management, leading to more robust code.
### Database Operations:

I consulted ChatGPT on how to implement database interactions using both MongoDB and PostgreSQL, which streamlined my approach to data storage.

### Advantages of Using AI
#### Speed and Efficiency:

AI significantly sped up the coding process by providing instant code snippets and solutions, which saved a considerable amount of time.
#### Knowledge Base:

With access to a vast amount of information, ChatGPT helped fill gaps in my understanding of complex concepts, particularly related to design patterns and database management.
#### Error Reduction:

By suggesting best practices and efficient coding techniques, AI helped minimize potential errors and improve code quality.

### Disadvantages of Using AI
#### Over-reliance:

There is a risk of becoming overly dependent on AI for problem-solving, which may hinder the development of critical thinking and coding skills.
#### Context Limitations:

Sometimes, the AI struggled to understand the specific context of my project, leading to suggestions that were not entirely applicable. This required additional effort to refine the code.
#### Lack of Personal Touch:

While AI can provide efficient solutions, it lacks the ability to understand the nuances of my unique coding style or project requirements fully.

### Prompts for Implementing Classes and Design Patterns
#### Creating a User Class:

- **Prompt**: "Can you help me create a ``User`` class in Python that has attributes for email, password, first name, and last name? Please include a method to set user details and another to return user information as a dictionary."
#### Implementing the Repository Pattern:

- **Prompt**: "I need to implement the Repository Pattern for a PostgreSQL database in Python. Can you provide a class called ``PostgresRepository`` with methods for creating, reading, updating, and deleting records? Make sure to include error handling in these methods."
#### Creating a Factory for Analysis Components:

- **Prompt**: "I want to implement a Factory Method pattern to create different analysis components like sentiment analysis, community detection, and graph representation in Python. Can you write a class ``AnalysisFactory`` with a static method ``create_analysis_component`` that returns an instance of the requested component type?"
#### Building a Controller Class with Dependency Injection:

- **Prompt**: "Can you help me write a ``ControllerUser`` class in Python that uses Dependency Injection? This class should handle user registration and login using a view and a repository. Make sure to include methods for adding a user and logging in a user, along with the necessary checks."
#### Implementing a Data Transfer Object (DTO):

- **Prompt**: "I need a DTO class called ``AnalysisResults`` in Python to hold the results of sentiment analysis, community detection, and graph generation. Can you create this class with an initializer to set these values and a method to convert the results to a dictionary format?"
#### Simulating a Sentiment Analysis Class:

- **Prompt**: "Can you write a ``SentimentAnalysis`` class in Python that includes a method analyze to simulate sentiment scoring? The method should return a sentiment score between -1 and 1 and also store a timestamp for when the analysis was conducted."
#### Creating a Community Detection Class:

- **Prompt**: "I need a ``CommunityDetection`` class in Python that simulates detecting communities from a dataset. Can you provide a method ``detect_communities`` that returns a list of detected communities along with a timestamp?"
#### Graph Representation Class:

- **Prompt**: "Can you help me create a ``GraphRepresentation`` class in Python that simulates graph generation? Include a method ``generate_graph`` that creates a placeholder graph and returns it along with a polarization level and timestamp."
#### Implementing Error Handling in Repository Classes:

- **Prompt**: "I want to enhance my ``MongoRepository`` class in Python with proper error handling. Can you show me how to implement try-except blocks in methods for creating, reading, updating, and deleting data?"

