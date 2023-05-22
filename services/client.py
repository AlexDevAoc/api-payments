from models.client import Client
from config.db import Session
from schemas.client import ClientResponse
from sqlalchemy import select

async def get_clients():
    with Session() as session: 
        clients = session.scalars(select(Client)).all()
        # Mapear los resultados a la estructura del schema de respuesta
        response = [ClientResponse(id=client.id, name=client.name, bank_provider_id=client.bank_provider_id,
                       created_at=client.created_at, updated_at=client.updated_at) for client in clients]

    return response
