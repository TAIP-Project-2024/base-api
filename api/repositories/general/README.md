# **Security and Debugging Component with AOP in Python**

This project implements a **Security and Debugging Component** using **Aspect-Oriented Programming (AOP)** principles. The security and AOP functionality is centralized and implemented in the `security_aop.py` file, ensuring secure file handling and debugging capabilities. It integrates MongoDB's GridFS to manage file storage securely while maintaining comprehensive logging for debugging purposes.

---

## **Features**

### **1. Security Component**
The code ensures a robust **security layer** by:
- **Input Validation**:
  - Prevents directory traversal attacks by validating filenames (e.g., blocking inputs like `../`).
  - Ensures all filenames are sanitized before interacting with the database.
- **Centralized Security Enforcement**:
  - The `@logging_and_security` decorator, implemented in `security_aop.py`, acts as an aspect to enforce security rules consistently across all repository operations.

---

### **2. Debugging Component**
Comprehensive logging is integrated as a **debugging tool**:
- **Logs Method Calls**:
  - Logs method names and arguments at every call.
  - Captures success or failure of operations.
  - Includes error messages for exceptions.
- **Simplified Debugging**:
  - Centralized logging through the `@logging_and_security` decorator ensures consistent and reusable logs.

---

### **3. AOP Integration**
The project applies **Aspect-Oriented Programming** principles:
- **Separation of Concerns**:
  - Cross-cutting concerns (security and debugging) are abstracted using the `@logging_and_security` decorator, which is implemented in `security_aop.py`.
  - Keeps the business logic of repository classes clean and focused.
- **Modularity**:
  - The decorator is reusable and extensible for additional repositories or functionalities.

---

## **Complexity and Scalability**
The component demonstrates **reasonable complexity** through:
- **Integration of MongoDB's GridFS**:
  - Supports non-trivial file storage and retrieval.
- **Advanced Programming Techniques**:
  - Uses Python decorators to implement AOP principles.
- **Scalability**:
  - The modular design ensures easy extension of security and debugging features.

---

## **Usage**
1. **Repository Initialization**:
   - Initialize the `DrawingRepository` or `GraphRepository` to manage files.
   - Example: 
     ```python
     drawing_repo = DrawingRepository()
     graph_repo = GraphRepository()
     ```
   
2. **Operations**:
   - Add, retrieve, update, or delete files using the respective repository methods.
   - Example:
     ```python
     with open("example.graphml", "rb") as file:
         graph_id = graph_repo.add("ExampleGraph", file)
         print(f"Graph added with ID: {graph_id}")
     ```

3. **Decorator Benefits**:
   - Logs every action and ensures secure inputs automatically via the `@logging_and_security` decorator from `security_aop.py`.

---

## **Alignment with Requirements**
This component meets the project requirements by:
- **Security**:
  - Validates inputs and prevents malicious attacks.
  - Centralizes security enforcement using AOP.
- **Debugging**:
  - Implements detailed logging for debugging method calls, arguments, and outcomes.
- **AOP Principles**:
  - Encapsulates cross-cutting concerns in a reusable decorator for modular and maintainable code.

---
