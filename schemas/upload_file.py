from pydantic import FilePath, BaseModel

class UploadResponse(BaseModel):
    DatosInsertadosCorrectamente: str
    MontosIncorrectos: str
    DatosIncorrectos: str

class DownloadResponse(BaseModel):
    file: FilePath