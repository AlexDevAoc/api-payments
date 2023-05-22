from models.payments import Payment
from sqlalchemy import func
from config.db import Session
from schemas.payment import PaymentResponse
from sqlalchemy import select
from fastapi.responses import JSONResponse

async def get_payments():

    with Session() as session:
        payments = session.scalars(select(Payment)).all()
        # Mapear los resultados a la estructura del schema de respuesta
        response = [PaymentResponse(id=payment.id, amount=payment.amount, payment_date=payment.payment_date, client_id=payment.client_id, 
                       created_at=payment.created_at, updated_at=payment.updated_at) for payment in payments]
    return response

def get_total_amount():
    with Session() as session:
        #Obtener todos los montos sumarlos y retornarlos
        total_amount = session.scalar(select(func.sum(Payment.amount).label("totalAmount")))
    return JSONResponse(content={"Total_Pagos_Recibidos": str(total_amount)})
