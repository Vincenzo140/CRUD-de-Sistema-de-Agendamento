from pydantic import BaseModel
from typing import List
from schemas.SchemaAgendamentoPost import ItemAgendamento

class GetAllAgendamentos(BaseModel):
    """Schema para exibir todo os posts."""

    agendamento: List[ItemAgendamento]
    
    class Config:
            json_schema_extra = {
                "example": {
                    "agendamento": [
                        {
                            "id": "1",
                            "date": "2024-01-01",
                            "horario": "12:00:00",
                            "cliente": "joao",
                            "servico": "cabelo",
                            "profissional": "carlos"
                        },
                    ]
                }
            }
class GetByIdAgendamentos(ItemAgendamento):
    """Schema para exibir um post."""
    id: str  # ID único do post

    class Config:
        schema_extra = {
            "example": {
                
                "id": "1",
                "date": "2024-01-01",
                "horario": "12:00:00",
                "cliente": "joao",
                "servico": "cabelo",
                "profissional": "carlos"
            }
        }            