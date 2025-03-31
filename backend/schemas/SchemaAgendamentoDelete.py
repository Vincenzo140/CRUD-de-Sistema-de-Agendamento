from pydantic import BaseModel



class DeleteAgendamento(BaseModel):
    """Modelo para representar a exclusão de um contato."""
    id: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": "1"
            }
        }