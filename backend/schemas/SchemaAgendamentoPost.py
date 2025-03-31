from pydantic import BaseModel
from typing import Optional

class PostAgendamento(BaseModel):
    data: str
    horario: str 
    cliente: str
    servico: str
    profissional: Optional[str] = None

    # Quando criar um agendamento, certifique-se de que o horário seja uma string
    @classmethod
    def from_orm(cls, obj):
        data = super().from_orm(obj)
        data.horario = str(obj.horario)  # Converte o horário para string
        return data


class ItemAgendamento(BaseModel):
    id: str  # O ID UUID entao deve ser string
    data: str
    horario: str
    cliente: str
    servico: str

    # Também convertendo o horário para string
    @classmethod
    def from_orm(cls, obj):
        data = super().from_orm(obj)
        data.horario = str(obj.horario)  # Converte o horário para string
        return data
