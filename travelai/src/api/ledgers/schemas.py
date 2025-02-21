from enum import Enum

# App-specific operations
# if app needs to add more operations, they can be added here
class ExtraLedgerOperation(Enum):
    CONTENT_CREATION = "CONTENT_CREATION"
    CONTENT_ACCESS = "CONTENT_ACCESS"

class TravelAILedgerOperation(Enum):
    pass
