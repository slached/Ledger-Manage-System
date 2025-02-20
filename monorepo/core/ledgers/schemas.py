from enum import Enum


class BaseLedgerOperation(Enum):
    # How to make sure that all ledger operations that inherits from BaseLedgerOperation have all of the SharedLedgerOperations defined below?
    CONTENT_CREATION = "CONTENT_CREATION"
    CONTENT_ACCESS = "CONTENT_ACCESS"


class SharedLedgerOperation(Enum):
    # shared ledger operations must contain all of the BaseLedgerOperations so end of the story
    # here is all operation that we can make on the ledger
    CONTENT_CREATION = BaseLedgerOperation.CONTENT_CREATION
    CONTENT_ACCESS = BaseLedgerOperation.CONTENT_ACCESS
    # extended operations
    DAILY_REWARD = "DAILY_REWARD"
    SIGNUP_CREDIT = "SIGNUP_CREDIT"
    CREDIT_SPEND = "CREDIT_SPEND"
    CREDIT_ADD = "CREDIT_ADD"
