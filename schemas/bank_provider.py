from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class BankProviderResponse(BaseModel):
    id: Optional[int]
    name: str
    created_at: datetime
    updated_at: datetime