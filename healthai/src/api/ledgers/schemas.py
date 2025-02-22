from enum import Enum
from pydantic import BaseModel
from itertools import chain
from monorepo.core.ledgers.schemas import BaseLedgerOperation


# App-specific operations
# if app needs to add more operations, they can be added here
class ExtraLedgerOperation(Enum):
    CONTENT_CREATION = "CONTENT_CREATION"
    CONTENT_ACCESS = "CONTENT_ACCESS"


HealthAILedgerOperation: Enum = Enum(
    "HealthAILedgerOperation",
    [(i.name, i.value) for i in chain(BaseLedgerOperation, ExtraLedgerOperation)],
)


# Validation section
class CreateOwnerBody(BaseModel):
    name: str
    surname: str


class AddLedgerEntryBody(BaseModel):
    owner_id: str
    ledger_operation: HealthAILedgerOperation
    nonce: str
