from enum import Enum, IntEnum
from itertools import chain
from pydantic import BaseModel

# import apps extra operations enum
from healthai.src.api.ledgers.schemas import (
    ExtraLedgerOperation as HealthAIExtraLedgerOperation,
)


class BaseLedgerOperation(Enum):
    # Base operations
    DAILY_REWARD = "DAILY_REWARD"
    SIGNUP_CREDIT = "SIGNUP_CREDIT"
    CREDIT_SPEND = "CREDIT_SPEND"
    CREDIT_ADD = "CREDIT_ADD"


# this contains all app's operations
# whenever new app added, they must add in chain too
LedgerOperation: Enum = Enum(
    "LedgerOperation",
    [
        (i.name, i.value)
        for i in chain(BaseLedgerOperation, HealthAIExtraLedgerOperation)
    ],
)
# Base + HealthAI extra operations
HealthAILedgerOperation: Enum = Enum(
    "HealthAILedgerOperation",
    [
        (i.name, i.value)
        for i in chain(BaseLedgerOperation, HealthAIExtraLedgerOperation)
    ],
)


# Validation section
# Response validators
class InsertResponse(BaseModel):
    msg: str
    status_code: int


class OwnerResponse(BaseModel):
    owner: list
    status_code: int


# Body Validators
class HealthAIAddLedgerEntryBody(BaseModel):
    owner_id: str
    ledger_operation: HealthAILedgerOperation
    nonce: str


class CreateOwnerBody(BaseModel):
    name: str
    surname: str
    balance: int


# These are the values of each ledger operation
class LedgerOperationConf(IntEnum):
    DAILY_REWARD = 1
    SIGNUP_CREDIT = 3
    CREDIT_SPEND = -1
    CREDIT_ADD = 10
    CONTENT_CREATION = -5
    CONTENT_ACCESS = 0
