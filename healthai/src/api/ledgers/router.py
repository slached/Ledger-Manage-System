from fastapi import APIRouter
from pydantic import BaseModel

from monorepo.core.ledgers.services.base_ledger_service import BaseLedgerService
from monorepo.core.ledgers.schemas import SharedLedgerOperation

router = APIRouter()
ledger_service = BaseLedgerService()

# Example endpoint
@router.post("/ledger")
def add_ledger_entry(operation: SharedLedgerOperation, owner_id: str, nonce: str):
    return ledger_service.create_ledger()
