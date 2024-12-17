import logging
from functools import wraps

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

# Validator to ensure secure filenames
def validate_filename(filename):
    if not isinstance(filename, str) or ".." in filename or "/" in filename or "\\" in filename:
        raise ValueError("Invalid filename detected.")
    return filename

# Decorator for logging and security
def logging_and_security(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            # Extract the function name and parameters
            method_name = func.__name__
            logging.info(f"Executing {method_name} with args: {args} kwargs: {kwargs}")

            # Validate filenames
            if "name" in kwargs:
                validate_filename(kwargs["name"])
            if len(args) > 1 and isinstance(args[1], str):  # If the first parameter is a name
                validate_filename(args[1])

            # Call the actual function
            result = func(*args, **kwargs)

            # Log the result
            logging.info(f"Method {method_name} executed successfully.")
            return result
        except Exception as e:
            logging.error(f"Error in {func.__name__}: {e}")
            raise
    return wrapper
