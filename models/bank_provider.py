from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config.db import Base

class BankProvider(Base):
    __tablename__ = 'bank_provider'
    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.current_timestamp())
    client = relationship("Client", back_populates="bank_provider")

