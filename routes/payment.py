from fastapi import APIRouter
from schemas.payment import PaymentResponse, PaymentTotalResponse
from typing import List
from services.payment import get_payments, get_total_amount

router = APIRouter()

@router.get("/payments",
            tags=["Payments"],
            response_model=List[PaymentResponse],
            description="Get a list of all payments")
async def get_all_payments():
    return await get_payments()

@router.get("/get_total_payments",
            tags=["Payments"],
            response_model=PaymentTotalResponse,
            description="Get all payments received")
def get_all_payments_received():
    return get_total_amount()
