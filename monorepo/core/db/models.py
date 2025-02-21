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
    created_on = Column(DateTime, default=func.now(), nullable=False)


class Owners(Base):
    __tablename__ = "owners"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    created_on = Column(DateTime, default=func.now(), nullable=False)
