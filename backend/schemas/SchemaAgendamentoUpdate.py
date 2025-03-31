from typing import Optional
from pydantic import BaseModel


class UpdateAgendamento(BaseModel):
    data: Optional[str] = None
    horario: Optional[str] = None
    cliente: Optional[str] = None
    servico: Optional[str] = None
