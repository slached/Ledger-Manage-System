from enum import Enum
from itertools import chain

# import all the extra operations from the applications
from healthai.src.api.ledgers.schemas import ExtraLedgerOperation


class BaseLedgerOperation(Enum):
    DAILY_REWARD = "DAILY_REWARD"
    SIGNUP_CREDIT = "SIGNUP_CREDIT"
    CREDIT_SPEND = "CREDIT_SPEND"
    CREDIT_ADD = "CREDIT_ADD"


# this is the model that will be used in the db
class LedgerOperation(Enum):
    Idx = Enum(
        "Idx",
        [(i.name, i.value) for i in chain(BaseLedgerOperation, ExtraLedgerOperation)],
    )
