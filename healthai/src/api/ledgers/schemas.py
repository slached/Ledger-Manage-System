from monorepo.core.ledgers.schemas import LedgerOperation
from enum import Enum


class HealthAILedgerOperation(Enum):
    # Base operations
    _base_operations = {op.name: op.value for op in LedgerOperation}

    # App-specific operations
    # if app needs to add more operations, they can be added here
    _extra_operations = {
        "CONTENT_CREATION": "CONTENT_CREATION",
        "CONTENT_ACCESS": "CONTENT_ACCESS",
    }
    locals().update(_base_operations)
    locals().update(_extra_operations)
