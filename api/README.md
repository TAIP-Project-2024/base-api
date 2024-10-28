
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

## Design Patterns Used

### Template Pattern

- The **Template Design Pattern** is used to define a base repository interface for database.
- The concrete classes, **MongoDBRepository** and **PostgresRepository** implement the base methods defined in template.
- This allows flexibility in the underlying database logic.
- It is present in **DbTemplate** class

### Repository Pattern

- The **Repository Design Pattern** creates and abstraction layer for data access.
- This pattern encapsulates the logic required to access data.
- It isolates data access logic from business logic.
- It is used in **MongoDBRepository** and **PostgresRepository** classes.

### Connection Pool Pattern

- The **Connection Pool Design Pattern** manages the database connections efficiently.
- It allows the reuse of connections and provides scalability.
- It is useful in a concurrent environments.
- It is used in **PostgreSQLConnectionPool** and **MongoDBClient**
- **For PostgreSQL:** When a connection is needed, a connection can be obtained by using the `connection = pool.getconn()` method (to release them back, just use `pool.putconn(connection)`).
- **For MongoDB:** The pool of connections is initialized by `client = MongoClient()`. MongoClient will automatically manage the connections. To close the pool, use `client.close()`.

### Active Record Pattern

- The **Active Record Design Pattern** is an architectural pattern to accessing data in a database
- A database table is wrapped into a class
- This pattern is used by object-relational mapping (ORM) by default

## Singleton vs Connection Pool

### Singleton

- Advantages: 
  - Easy to implement and use
  - Reduces memory usage
- Disadvantages:
  - Doesn't efficiently manage multiple database connections

### Connection Pool
- Advantages:
  - Provides better scalability
  - Efficiently manages database connections
- Disadvantages:
  - Requires careful management of the pool size and connection limits to avoid exhaustion

Given the nature of this application, which includes a real-time dashboard, a **Connection Pool** might be a better choice due to the fact that:
- it handles simultaneous requests efficiently
- it can handle more users simultaneously
- it provides better control over the database resources

## AI Usage (ChatGPT)

### Advantages:
- It can be helpful in providing simple explanations.
- It offers sample code that is relatively easy to follow.
- It provides useful and well-structured information (e.g., the comparison between Singleton and Connection Pool)

### Disadvantages:
- Sometimes, it does not provide contextual answers and, instead, it gives out-of-context examples
- Regarding MVC, it can confuse the concepts of model and controller, which can lead to misunderstanding without prior knowledge
- It's easy to become overly reliant on its responses

### AI prompts

**Q:**: this is the requirement analysis of our project. can I implement Template method for database connections? and to have concrete classes for each database? *(Among with this message, the content of Requirements Analysis file was provided)* <br>
**A:** Yes, you can definitely implement the Template Method pattern for your database connections in this context. Here’s how you could approach it:
Template Method Pattern for Database Connections
Define a Base Template Class: Create an abstract base class that defines the essential methods for database operations (e.g., create, get, update, delete, close).
Concrete Classes: Implement concrete classes for each type of database you want to support. Each class will implement the methods defined in the base class according to the specifics of the respective database. <br>


**Q:** knowing the requirements analysis mentioned above, what would you choose for db connection: singleton or connection pool? <br>
**A:** Choosing between a Singleton pattern and a Connection Pool for managing database connections depends on the specific needs and characteristics of your application. Given your requirements, here’s a breakdown of each option:
Singleton Pattern
Definition: The Singleton pattern ensures that a class has only one instance and provides a global point of access to that instance.
Use Case: Suitable for scenarios where a single instance of a resource is needed throughout the application's lifecycle, such as configuration settings or logging.
Advantages:
Easy to implement and use.
Reduces memory usage since there’s only one instance.
Disadvantages:
Can become a bottleneck in high-concurrency scenarios where multiple threads try to access the single instance simultaneously.
Doesn't efficiently manage multiple database connections, especially in applications with high traffic.
Connection Pool
Definition: A connection pool maintains a set of database connections that can be reused, rather than opening a new connection for every database request.
Use Case: Ideal for applications with multiple simultaneous database requests, like web applications with high concurrency.
Advantages:
Efficiently manages database connections, reducing overhead from frequently opening and closing connections.
Improves performance by allowing multiple requests to use available connections from the pool.
Provides better scalability, especially under high load.
Disadvantages:
More complex to implement than a Singleton.
Requires careful management of the pool size and connection limits to avoid exhaustion.
Recommendation for Your Application
Given the requirements of your application, which includes a real-time dashboard that fetches live social media data and analyzes sentiment, a Connection Pool is the better choice for several reasons:
High Concurrency: Your application will likely handle multiple simultaneous requests for data fetching, preprocessing, and analysis. A connection pool can manage these concurrent connections effectively.
Performance: Reusing connections from a pool can significantly enhance performance compared to opening and closing connections for each database operation.
Scalability: As your application grows and potentially handles more data or users, a connection pool will allow you to scale better without the bottleneck of a single database connection.
Resource Management: It provides better control over database resources, ensuring that you’re not exceeding the database’s connection limits.
Conclusion
In summary, for a real-time dashboard application with high concurrency needs and frequent database interactions, implementing a Connection Pool will be more efficient and scalable than using a Singleton pattern for database connections. If you have any further questions or need more details, feel free to ask! <br>

**Q:** what design patterns are integrated in django ORM? <br>
**A:** Django ORM integrates elements of the Active Record design pattern. In the Active Record pattern, an object represents a row in a database table, and the object's methods are used to interact with the database. This is why Django models can directly save, update, delete, and query data using methods like .save(), .update(), .delete(), and .objects.filter().
This approach contrasts with the Repository pattern, where data access logic is fully separated from the objects themselves. Django ORM's Active Record implementation keeps data operations closer to the models, simplifying interactions for developers, especially in CRUD operations. However, it can limit flexibility, particularly in complex applications with multiple data sources or advanced business logic needs.
If you need more decoupling between business logic and data access in Django, you can create custom repositories or services to encapsulate data logic separately.


