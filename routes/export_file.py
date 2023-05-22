from fastapi import APIRouter
from config.db import Session
from services.export_file import export_data
from schemas.upload_file import DownloadResponse

router = APIRouter()
session = Session()

@router.get(
        "/download",  
        tags=["ManageFiles"],
        response_model=DownloadResponse,
        description="Download payments data on excel file")
def download_file():
    return export_data()