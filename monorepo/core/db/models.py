from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum, func
from ..db import Base
from ..ledgers.schemas import LedgerOperation


class Ledgers(Base):
    __tablename__ = "ledgers"

    id = Column(Integer, primary_key=True, index=True)
    operation = Column(Enum(LedgerOperation), nullable=False)
    amount = Column(Boolean, nullable=False)
    nonce = Column(String, nullable=False)
    owner_id = Column(String, nullable=False)
    created_on = Column(DateTime, default=func.localtime(), nullable=False)
