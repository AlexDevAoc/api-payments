from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os 
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DB_NAME:str = os.getenv('DB_NAME')
    DB_USER:str = os.getenv('DB_USER')
    DB_PASSWORD:str = os.getenv('DB_PASSWORD')
    DB_HOST:str = os.getenv('DB_HOST')
    DB_PORT:str = os.getenv('DB_PORT')
    DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

settings = Settings()

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Session = sessionmaker(engine)
Base = declarative_base() 

