from fastapi import UploadFile
from fastapi.responses import JSONResponse
from models.bank_provider import BankProvider
from models.client import Client
from models.payments import Payment
from config.db import Session
import pandas as pd

session = Session()


async def upload_excel(file: UploadFile):
    try:
        # Leer el archivo Excel y obtener los datos
        df = pd.read_excel(file.file)
        session.begin()
        # Insertar datos en la tabla BankProvider
        bank_providers = []
        # _ es una variable que representa el indice del documento
        for _, row in df["Proveedor"].items():
            # Realizar la consulta para verificar si el nombre del proveedor ya existe
            proveedor_existente = session.query(BankProvider).filter_by(name=row).first()
            if proveedor_existente == None:
                bank_provider = BankProvider(name=row)
                bank_providers.append(bank_provider)
                session.add_all(bank_providers)
                session.commit()

        # Insertar datos en la tabla Client
        clients = []
        for _, row in df.iterrows():
            bank_provider = session.query(BankProvider).filter_by(
                name=row["Proveedor"]).first()
            client = Client(name=row["Cliente"], bank_provider_id=bank_provider.id)
            clients.append(client)
        session.add_all(clients)
        session.commit()
        
        # Insertar datos en la tabla Payment
        counterCorrectAmount = 0
        payments = []
        counterAmountErrors = 0
        incorrectsPayments = []
        for _, row in df.iterrows():
            client = session.query(Client).filter_by(name=row["Cliente"]).first()
            # Validar si el monto es incorrecto
            if type(row["Monto"]) == str:
                counterAmountErrors += 1
                incorrectPayment = {"Monto": row["Monto"], "Cliente": row["Cliente"]}
                incorrectsPayments.append(incorrectPayment)
            else:
                counterCorrectAmount += 1
                payment = Payment(amount=row["Monto"], payment_date=row["Fecha"], client_id=client.id)
                payments.append(payment)            
        session.add_all(payments)
        session.commit()
        return JSONResponse(content={"DatosInsertadosCorrectamente": str(counterCorrectAmount), 
                                     "MontosIncorrectos": str(counterAmountErrors), 
                                     "DatosIncorrectos": str(incorrectsPayments)})

    except Exception as e:
        session.rollback()
        session.commit()
        raise JSONResponse(content={"Error": "Error al procesar el archivo Excel", "DetalleError": str(e)}, status_code=500)
    
