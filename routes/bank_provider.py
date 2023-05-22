from fastapi import APIRouter
from schemas.bank_provider import BankProviderResponse
from typing import List
from services.bank_provider import get_bankProviders

router = APIRouter()

@router.get("/bankproviders", 
            tags=["BankProviders"],
            response_model= List[BankProviderResponse],
            description="Get a list of all bankProviders")
async def get_all_bank_providers():
    return await get_bankProviders()
