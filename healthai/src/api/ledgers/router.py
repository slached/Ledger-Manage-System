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


# Creates ledger entry
@router.post("/ledger")
def add_ledger_entry(
    body: HealthAIAddLedgerEntryBody, db: Session = Depends(get_db)
) -> InsertResponse:
    ledger_service = BaseLedgerService(db)
    return ledger_service.create_ledger(body=body)


# Gets owner's balance
@router.get("/ledger/{owner_id}")
def get_owner_balance(owner_id, db: Session = Depends(get_db)) -> GetBalanceResponse:
    ledger_service = BaseLedgerService(db)
    return ledger_service.get_owner_balance(owner_id=owner_id)
