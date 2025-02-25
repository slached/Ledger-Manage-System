from enum import Enum, IntEnum
from pydantic import BaseModel

# import apps extra operations enum
from healthai.src.api.ledgers.schemas import (
    ExtraLedgerOperation as HealthAIExtraLedgerOperation,
)
from travelai.src.api.ledgers.schemas import (
    ExtraLedgerOperation as TravelAIExtraLedgerOperation,
)


class BaseLedgerOperation(Enum):
    # Base operations
    DAILY_REWARD = "DAILY_REWARD"
    SIGNUP_CREDIT = "SIGNUP_CREDIT"
    CREDIT_SPEND = "CREDIT_SPEND"
    CREDIT_ADD = "CREDIT_ADD"


# this contains all app's operations
# whenever new app added, they must add in chain too
unique_names = {}
for enum_class in [
    BaseLedgerOperation,
    HealthAIExtraLedgerOperation,
    TravelAIExtraLedgerOperation,
]:
    for i in enum_class:
        if i.name not in unique_names:
            unique_names[i.name] = i.value

LedgerOperation = Enum("LedgerOperation", unique_names)

# Base + HealthAI extra operations
unique_names = {}
for enum_class in [
    BaseLedgerOperation,
    HealthAIExtraLedgerOperation,
]:
    for i in enum_class:
        if i.name not in unique_names:
            unique_names[i.name] = i.value

HealthAILedgerOperation = Enum("HealthAILedgerOperation", unique_names)

# Base + TravelAI extra operations
unique_names = {}
for enum_class in [
    BaseLedgerOperation,
    TravelAIExtraLedgerOperation,
]:
    for i in enum_class:
        if i.name not in unique_names:
            unique_names[i.name] = i.value

TravelAILedgerOperation = Enum("TravelAILedgerOperation", unique_names)


# Validation section
# Response validators
class InsertResponse(BaseModel):
    msg: str
    id: int
    status_code: int


class OwnerResponse(BaseModel):
    owner: list
    status_code: int


class GetBalanceResponse(BaseModel):
    balance: int
    status_code: int


# Body Validators
class HealthAIAddLedgerEntryBody(BaseModel):
    owner_id: str
    ledger_operation: HealthAILedgerOperation  # type: ignore
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
