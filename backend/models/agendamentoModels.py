from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import uuid

db = SQLAlchemy()

class Agendamento(db.Model):
    __tablename__ = 'agendamentos'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    data = db.Column(db.Date, nullable=False)
    horario = db.Column(db.Time, nullable=False)
    cliente = db.Column(db.String(100), nullable=False)
    servico = db.Column(db.String(100), nullable=False)
