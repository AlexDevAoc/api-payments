from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class PaymentResponse(BaseModel):
    id: Optional[int]
    amount: float
    payment_date: datetime
    client_id: int
    created_at: datetime
    updated_at: datetime

class PaymentTotalResponse(BaseModel):
    Total_Pagos_Recibidos: str