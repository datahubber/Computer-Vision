from pydantic import BaseModel
from pydantic.alias_generators import to_camel

class Result(BaseModel):
    """Result class to represent the output of a request. 
    Request can be either command or query class.
    """
    
    success: bool
    error: str | None = None
    model_config = {
        "alias_generator": to_camel,
        "populate_by_name": True,
        "protected_namespaces": (),
    }

    @staticmethod
    def succeed() -> "Result":
        """Return a successful result"""
        return Result(success=True)
    
    @staticmethod
    def fail(error: str | None) -> "Result":
        """Return a failed result"""
        return Result(success=False, error=error or "An error occurred")
    

class ResultWithData[TData](Result):
    """Result class with payload"""

    data: TData | None = None
    """Payload of the result"""

    @staticmethod
    def succeed(payload: TData) -> "ResultWithData[TData]": # type: ignore
        """Return a successful result with payload"""
        return ResultWithData[TData](success=True, data=payload)
    
    @staticmethod
    def fail(error: str | None) -> "ResultWithData[TData]":
        """Return a failed result"""
        return ResultWithData[TData](success=False, error=error or "An error occurred")
    

class ResultWithArray[TData](ResultWithData[list[TData]]):
    """Result class with array payload.
    This class equivalent to `ResultWithData[list[TData]]` but with a more descriptive name and shorter syntax.
    For example, `ResultWithArray[int]` is equivalent to `ResultWithData[list[int]]`.
    """

    @staticmethod
    def succeed(payload: list[TData]) -> "ResultWithArray[TData]":
        """Return a successful result with payload"""
        return ResultWithArray[TData](success=True, data=payload)
    
    @staticmethod
    def fail(error: str | None) -> "ResultWithArray[TData]":
        """Return a failed result"""
        return ResultWithArray[TData](success=False, error=error or "An error occurred")