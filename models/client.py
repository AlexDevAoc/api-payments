from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config.db import Base

class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.current_timestamp())
    bank_provider_id = Column(Integer, ForeignKey('bank_provider.id'))
    bank_provider = relationship("BankProvider", back_populates="client")
    payment = relationship("Payment", back_populates="client")

