from enum import Enum
from itertools import chain

# import apps extra operations enum
from healthai.src.api.ledgers.schemas import ExtraLedgerOperation


class BaseLedgerOperation(Enum):
    # Base operations
    DAILY_REWARD = "DAILY_REWARD"
    SIGNUP_CREDIT = "SIGNUP_CREDIT"
    CREDIT_SPEND = "CREDIT_SPEND"
    CREDIT_ADD = "CREDIT_ADD"


# this contains all app's extra operations
# if any app has more operations, they must be in chain
LedgerOperation: Enum = Enum(
    "LedgerOperation",
    [(i.name, i.value) for i in chain(BaseLedgerOperation, ExtraLedgerOperation)],
)
