from fastapi import HTTPException


class NotFoundException(HTTPException):
    def __init__(self, detail="Resource not found"):
        super().__init__(status_code=404, detail=detail)


class DatabaseException(HTTPException):
    def __init__(self, detail="Database error"):
        super().__init__(status_code=500, detail=detail)


class SufficientBalanceException(HTTPException):
    def __init__(self, detail="Balance sufficient"):
        super().__init__(status_code=400, detail=detail)
