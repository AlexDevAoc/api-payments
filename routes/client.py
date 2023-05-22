from fastapi import APIRouter
from schemas.client import ClientResponse
from typing import List
from services.client import get_clients

router = APIRouter()

@router.get(
    "/clients",
    tags=["Clients"],
    response_model= List[ClientResponse],
    description="Get a list of all clients")
async def get_all_clients():
    return await get_clients()
