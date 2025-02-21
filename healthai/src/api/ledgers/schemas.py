from enum import Enum

from monorepo.core.ledgers.schemas import BaseLedgerOperation


# App-specific operations
# if app needs to add more operations, they can be added here
class ExtraLedgerOperation(Enum):
    CONTENT_CREATION = "CONTENT_CREATION"
    CONTENT_ACCESS = "CONTENT_ACCESS"


class HealthAILedgerOperation(Enum):
    def __init__(self):
        _extra_operations = {op.name: op.value for op in ExtraLedgerOperation}
        # Base operations
        _base_operations = {op.name: op.value for op in BaseLedgerOperation}
        locals().update(_base_operations)
        locals().update(_extra_operations)
