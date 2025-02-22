from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from monorepo.core.ledgers.services.base_ledger_service import BaseLedgerService
from monorepo.core.db import get_db
from monorepo.core.ledgers.schemas import (
    HealthAIAddLedgerEntryBody,
    InsertResponse,
    GetBalanceResponse,
)

router = APIRouter()

# Different router activities goes here
