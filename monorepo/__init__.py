from fastapi import FastAPI, Depends, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from .core.ledgers.services.base_ledger_service import BaseLedgerService
from .core.db import get_db
from .core.ledgers.schemas import CreateOwnerBody, InsertResponse

from .core.ledgers.errors import (
    NotFoundException,
    DatabaseException,
    SufficientBalanceException,
)

# Router imports
# from travelai.src.api.ledgers import router as travelai
from healthai.src.api.ledgers import router as healthai

app = FastAPI()


# Global Error Handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error", "error": str(exc)},
    )


# Not Found Error Handler
@app.exception_handler(NotFoundException)
async def not_found_exception_handler(request: Request, exc: NotFoundException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )


# DataBase Error Handler
@app.exception_handler(DatabaseException)
async def database_exception_handler(request: Request, exc: DatabaseException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )


# Balance Error Handler
@app.exception_handler(SufficientBalanceException)
async def database_exception_handler(request: Request, exc: SufficientBalanceException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )


# monorepo specific controller
# creates owner
@app.post("/create_owner")
def create_owner(
    body: CreateOwnerBody, db: Session = Depends(get_db)
) -> InsertResponse:
    ledger_service = BaseLedgerService(db)
    return ledger_service.create_owner(body=body)


# app routers
app.include_router(healthai.router)
# app.include_router(travelai.router)
