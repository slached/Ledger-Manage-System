from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from monorepo.core.ledgers.services.base_ledger_service import BaseLedgerService
from .schemas import CreateOwnerBody, AddLedgerEntryBody
from monorepo.core.db import get_db

router = APIRouter()


@router.post("/create_owner")
def create_owner(body: CreateOwnerBody, db: Session = Depends(get_db)):
    ledger_service = BaseLedgerService(db)
    return ledger_service.create_owner(body=body)


@router.post("/ledger")
def add_ledger_entry(body: AddLedgerEntryBody, db: Session = Depends(get_db)):
    ledger_service = BaseLedgerService(db)
    return ledger_service.create_ledger(body=body)
