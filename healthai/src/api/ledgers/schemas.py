from enum import Enum
from pydantic import BaseModel


# App-specific operations
# if app needs to add more operations, they can be added here
class ExtraLedgerOperation(Enum):
    CONTENT_CREATION = "CONTENT_CREATION"
    CONTENT_ACCESS = "CONTENT_ACCESS"


# This way did not work
"""class HealthAILedgerOperation(Enum):
    def __init__(self):
        _extra_operations = {op.name: op.value for op in ExtraLedgerOperation}
        # Base operations
        _base_operations = {op.name: op.value for op in BaseLedgerOperation}
        locals().update(_base_operations)
        locals().update(_extra_operations)"""


class HealthAILedgerOperation(Enum):
    # Base operations
    DAILY_REWARD = "DAILY_REWARD"
    SIGNUP_CREDIT = "SIGNUP_CREDIT"
    CREDIT_SPEND = "CREDIT_SPEND"
    CREDIT_ADD = "CREDIT_ADD"

    # Extra operations goes here
    CONTENT_CREATION = "CONTENT_CREATION"
    CONTENT_ACCESS = "CONTENT_ACCESS"


# Validation section
class CreateOwnerBody(BaseModel):
    name: str
    surname: str


class AddLedgerEntryBody(BaseModel):
    owner_id: str
    ledger_operation: HealthAILedgerOperation
    nonce: str
