from sqlalchemy import Column, Integer, ForeignKey, DateTime, Double
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config.db import Base

class Payment(Base):
    __tablename__ = 'payment'
    id = Column(Integer, primary_key=True)
    amount = Column(Double)
    payment_date = Column(DateTime)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.current_timestamp())
    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship("Client", back_populates="payment")

