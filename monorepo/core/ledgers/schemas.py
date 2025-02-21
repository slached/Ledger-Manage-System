from enum import Enum

# import all the extra operations from the applications

# import is not working i dont know why so i will just copy the code
# from healthai.src.api.ledgers.schemas import ExtraLedgerOperation
# think that as a import statement


# this is the operation type that will be used in the db
# python has no interface so we will use this as a interface
# but enums cannot be inherited so we will use this as a base class
# also i research lot about this but i could not find a way to extend the operations
# from the other applications
# the only way is to changing enum type into string in db
class LedgerOperation(Enum):
    # Base operations
    DAILY_REWARD = "DAILY_REWARD"
    SIGNUP_CREDIT = "SIGNUP_CREDIT"
    CREDIT_SPEND = "CREDIT_SPEND"
    CREDIT_ADD = "CREDIT_ADD"

    # Extra operations goes here
    CONTENT_CREATION = "CONTENT_CREATION"
    CONTENT_ACCESS = "CONTENT_ACCESS"
