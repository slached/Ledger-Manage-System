from enum import Enum
from monorepo.core.ledgers.schemas import BaseLedgerOperation


# App-specific operations
# if app needs to add more operations, they can be added here
class ExtraLedgerOperation(Enum):
    CONTENT_CREATION = "CONTENT_CREATION"
    CONTENT_ACCESS = "CONTENT_ACCESS"
Idx = ExtraLedgerOperation

class TravelAILedgerOperation(Enum):
    pass
