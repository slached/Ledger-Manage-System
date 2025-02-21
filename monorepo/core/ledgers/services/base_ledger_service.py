from ...db.ledger_repository import LedgerRepository
from healthai.src.api.ledgers.schemas import CreateOwnerBody, AddLedgerEntryBody
from sqlalchemy.orm import Session


class BaseLedgerService:
    def __init__(self, db: Session):
        self.ledger_repository = LedgerRepository(db)

    def create_ledger(
        self,
        body: AddLedgerEntryBody,
    ):
        # Implementation
        pass

    def create_owner(
        self,
        body: CreateOwnerBody,
    ):
        return self.ledger_repository.InsertOwner(body)
