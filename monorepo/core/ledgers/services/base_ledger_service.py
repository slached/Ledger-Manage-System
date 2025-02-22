from ...db.ledger_repository import LedgerRepository
from ...ledgers.schemas import (
    HealthAIAddLedgerEntryBody,
    LedgerOperationConf,
    CreateOwnerBody,
    GetBalanceResponse,
)
from sqlalchemy.orm import Session
from ..errors import NotFoundException, SufficientBalanceException


class BaseLedgerService:
    def __init__(self, db: Session):
        self.ledger_repository = LedgerRepository(db)

    def get_owner(self, owner_id):
        # Try to find owner exists
        owner = self.ledger_repository.GetOwnerById(owner_id).owner
        if len(owner) == 0:
            raise NotFoundException(detail="Owner could not founded!")
        return owner[0]

    def get_owner_balance(self, owner_id):
        return GetBalanceResponse(
            balance=self.get_owner(owner_id=owner_id).balance, status_code=200
        )

    def create_owner(self, body: CreateOwnerBody):
        return self.ledger_repository.InsertOwner(body)

    def create_ledger(
        self,
        body: HealthAIAddLedgerEntryBody,
    ):

        owner = self.get_owner(body.owner_id)

        repo_body = {
            "owner_id": body.owner_id,
            "ledger_op": body.ledger_operation,
            "nonce": body.nonce,
        }

        for operation in LedgerOperationConf:
            if operation.name == body.ledger_operation.name:
                # if value greater than 0 that means we don't need to validate balance sufficiency
                # if value lesser than 0 and owner's balance lesser then operation's absolute value then
                # throw balance sufficient exception
                if operation.value < 0 and owner.balance < abs(operation.value):
                    raise SufficientBalanceException()
                else:
                    # add amount field after there is no any exception in transmission
                    repo_body.update(amount=owner.balance + operation.value)

        # first update owner balance
        self.ledger_repository.UpdateOwner(
            owner_id=owner.id, update_data={"balance": repo_body["amount"]}
        )
        # then create ledger entry
        return self.ledger_repository.InsertLedgerEntry(body=repo_body)
