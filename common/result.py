from typing import TypeVar, Generic

TValue = TypeVar('TValue')

class Result(Generic[TValue]):
    value: TValue
    error: str
    is_success: bool
    is_failure: bool

    def __init__(self, value: TValue, is_succes: bool, error: str):
        self.value = value
        self.is_success = is_succes
        self.is_failure = not is_succes
        self.error = error

    def success(value: TValue):
        return Result(value=value, is_succes=True, error=None)
    
    def failure(error: str):
        return Result(value=None, is_succes=False, error=error)
    
