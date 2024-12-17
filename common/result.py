from typing import TypeVar, Generic

TValue = TypeVar('TValue')

class Result(Generic[TValue]):
    """
        Result will be used as method return type for services and repositories.
    """

    value: TValue
    error: str
    is_success: bool
    is_failure: bool

    def __init__(self, value: TValue, is_success: bool, error: str):
        self.value = value
        self.is_success = is_success
        self.is_failure = not is_success
        self.error = error

    def success(value: TValue):
        return Result(value=value, is_success=True, error=None)
    
    def failure(error: str):
        return Result(value=None, is_success=False, error=error)
    
