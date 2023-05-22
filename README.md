# Ejecución en desarrollo

1. Clonar Repositorio
<br>
<br>

2. Ejecutar
```
pip install -r requirements.txt
```
<br>
3. Tener docker intalado o alguna instalacion de mysql

4. Clonar Archivo ```.env.template.dev``` y renombrarlo a ```.env``` modificar valores de acuerdo al ambiente.
```bash
#DB CONFIG
DB_HOST=
DB_PORT=
DB_USER=
DB_PASSWORD=
DB_NAME=
```
<br>

5. Levantar la DB con el siguiente comando (omitir este paso si no se usara docker)
```
docker-compose up -d
```
<br>

6. Levantar modo desarrollo 
```
uvicorn app:app --reload
```
<br>

7. Documentacion API
```
http://127.0.0.1:8000/docs
```
<br>

## Comandos para ejecutar la App

```bash
# development
$ uvicorn app:app

# watch mode
$ uvicorn app:app --reload

```

## Stack Utilizado
FastApi 0.95.2
SQLAlchemy 2.0
Python 3.11.3
