from ...db.ledger_repository import LedgerRepository
from ..schemas import SharedLedgerOperation
from pydantic import BaseModel


# Validation i will write a mw for validation but in this state thats ok
class CreateLedgerBody(BaseModel):
    owner_id: str
    ledger_operation: SharedLedgerOperation
    nonce: str


class BaseLedgerService:
    def __init__(self):
        # needs dependency injection
        self.ledger_repository = LedgerRepository()

    def create_ledger(
        self,
        body: CreateLedgerBody,
    ):
        # Implementation
        pass
