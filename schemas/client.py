from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class ClientResponse(BaseModel):
    id: Optional[int]
    name: str
    bank_provider_id: int
    created_at: datetime
    updated_at: datetime
