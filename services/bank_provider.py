from models.bank_provider import BankProvider
from config.db import Session
from sqlalchemy import select
from schemas.bank_provider import BankProviderResponse

async def get_bankProviders():
    with Session() as session:
        bank_providers = session.scalars(select(BankProvider)).all()
        # Mapear los resultados a la estructura del schema de respuesta
        response = [BankProviderResponse(id=bank_provider.id, name=bank_provider.name, created_at=bank_provider.created_at,
                                     updated_at=bank_provider.updated_at) for bank_provider in bank_providers]
    return response
