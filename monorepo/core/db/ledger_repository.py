from sqlalchemy.orm import Session
from ..db.models import Ledgers, Owners
from ..ledgers.schemas import InsertResponse, OwnerResponse, CreateOwnerBody


class LedgerRepository:

    def __init__(self, db: Session):
        self.db = db

    def InsertOwner(self, body: CreateOwnerBody):
        new_owner = Owners(name=body.name, surname=body.surname, balance=body.balance)
        self.db.add(new_owner)
        self.db.commit()
        self.db.refresh(new_owner)
        return InsertResponse(
            msg=f"{new_owner.id} created successfully.", status_code=201
        )

    def InsertLedgerEntry(self, body: dict):
        new_ledger = Ledgers(
            operation=body["ledger_op"].value,
            amount=body["amount"],
            nonce=body["nonce"],
            owner_id=body["owner_id"],
        )
        self.db.add(new_ledger)
        self.db.commit()
        self.db.refresh(new_ledger)

        return InsertResponse(
            msg=f"{new_ledger.id} created successfully.", status_code=201
        )

    def GetOwnerById(self, owner_id: str):
        # Find owner
        owner = self.db.query(Owners).filter(Owners.id == owner_id).all()
        return OwnerResponse(owner=owner, status_code=200)

    def UpdateOwner(self, owner_id: str, update_data: dict):
        # Update owner
        owner = self.db.query(Owners).filter(Owners.id == owner_id).update(update_data)
        return OwnerResponse(owner=[owner], status_code=200)
