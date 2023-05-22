from fastapi import APIRouter, UploadFile
from config.db import Session
from services.upload_file import upload_excel
from schemas.upload_file import UploadResponse


router = APIRouter()
session = Session()

@router.post(
        "/upload",  
        tags=["ManageFiles"],
        response_model=UploadResponse,
        description="Upload file to database")
async def upload_file(file: UploadFile):
    return await upload_excel(file)

