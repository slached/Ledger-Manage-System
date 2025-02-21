from healthai.src.api.ledgers.schemas import CreateOwnerBody, AddLedgerEntryBody
from .models import Owners
from sqlalchemy.orm import Session


class LedgerRepository:

    def __init__(self, db: Session):
        self.db = db

    def InsertOwner(self, body: CreateOwnerBody):
        new_owner = Owners(name=body.name, surname=body.surname)
        self.db.add(new_owner)
        self.db.commit()
        self.db.refresh(new_owner)
        return {"msg": f"{new_owner.id} is created", "status_code": 201}
