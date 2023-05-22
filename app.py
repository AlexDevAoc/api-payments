from fastapi import FastAPI
from routes import bank_provider, client, payment, upload_file, export_file
from config.db import Base, engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Payments API",
    description="Rest API for manage payments",
    version="0.0.1")

# Configuración de los orígenes permitidos (origins)
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://example.com",
    "http://example.com:8080",
]

# Configuración de los métodos HTTP permitidos (methods)
methods = ["GET", "POST"]

# Configuración de los encabezados permitidos (headers)
headers = [
    "Content-Type",
    "Authorization",
]

# Agregar el middleware de CORS a la aplicación
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=methods,
    allow_headers=headers,
    allow_credentials=True,  # Si se permiten las credenciales (cookies, encabezados de autorización, etc.)
    expose_headers=["Content-Disposition"],  # Encabezados personalizados expuestos
)
# Rutas
app.include_router(client.router)
app.include_router(payment.router)
app.include_router(bank_provider.router)
app.include_router(upload_file.router)
app.include_router(export_file.router)


# Creación de las tablas en la base de datos
Base.metadata.create_all(bind=engine)
