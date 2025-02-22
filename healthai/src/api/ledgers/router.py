from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from monorepo.core.ledgers.services.base_ledger_service import BaseLedgerService
from monorepo.core.db import get_db
from monorepo.core.ledgers.schemas import (
    HealthAIAddLedgerEntryBody,
    InsertResponse,
)

router = APIRouter()


#
@router.post("/ledger")
def add_ledger_entry(
    body: HealthAIAddLedgerEntryBody, db: Session = Depends(get_db)
) -> InsertResponse:
    ledger_service = BaseLedgerService(db)
    return ledger_service.create_ledger(body=body)
