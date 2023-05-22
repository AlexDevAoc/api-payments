from config.db import Session
from models.bank_provider import BankProvider
from models.client import Client
from models.payments import Payment
from fastapi.responses import FileResponse
import pandas as pd

def export_data():
    # Crear una sesión de la base de datos
    session = Session()

    # Obtener información de la base de datos
    results = (
    session.query(Payment.amount, Payment.payment_date, Client.name, BankProvider.name)
    .join(Client, Payment.client_id == Client.id)
    .join(BankProvider, Client.bank_provider_id == BankProvider.id)
    .all() 
    )
    # Crear un DataFrame de Pandas con los datos
    data = []
    # Iterar sobre los resultados
    for amount, payment_date, client_name, bank_provider_name in results:
             data.append({
            "Fecha": payment_date,
            "Cliente": client_name,
            "Monto": amount,
            "Proveedor": bank_provider_name
            })
    df = pd.DataFrame(data)
 
    # Guardar los datos en un archivo Excel
    excel_filename = "data_export.xlsx"
    df.to_excel(excel_filename, index=False)
    
    # Descargar el archivo de Excel como respuesta
    return FileResponse(excel_filename, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", 
                        headers={"Content-Disposition": "attachment;filename=all_payments.xlsx"})
 