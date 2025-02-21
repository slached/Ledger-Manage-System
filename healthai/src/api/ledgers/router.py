from fastapi import APIRouter

from monorepo.core.ledgers.services.base_ledger_service import BaseLedgerService
from .schemas import HealthAILedgerOperation

router = APIRouter()
ledger_service = BaseLedgerService()


# Example endpoint
@router.post("/ledger")
def add_ledger_entry(operation: HealthAILedgerOperation, owner_id: str, nonce: str):
    return ledger_service.create_ledger()
