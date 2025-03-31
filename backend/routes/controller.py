from flask import Blueprint, jsonify, request
from logger.logging import AppLogger
from schemas.SchemaAgendamentoDelete import DeleteAgendamento
from schemas.SchemaAgendamentoGet import GetAllAgendamentos, GetByIdAgendamentos
from schemas.SchemaAgendamentoPost import PostAgendamento, ItemAgendamento
from schemas.SchemaAgendamentoUpdate import UpdateAgendamento
from models.agendamentoModels import db, Agendamento
from datetime import datetime

logger = AppLogger().get_logger()
app = Blueprint('agendamentos', __name__)

@app.post("/agendamentos")
def create_agendamento():
    """
    Cria um novo agendamento no sistema.

    Espera os seguintes dados no corpo da requisição:
    - data: Data do agendamento.
    - horario: Horário do agendamento.
    - cliente: Nome do cliente.
    - servico: Serviço solicitado.

    Retorna o agendamento criado em formato JSON.

    Returns:
        Response: A resposta HTTP contendo o agendamento criado ou um erro.
    """
    try:
        data = request.get_json()
        agendamento = Agendamento(
            data=data["data"],
            horario=data["horario"],  # Certifique-se que 'data["horario"]' seja uma string
            cliente=data["cliente"],
            servico=data["servico"]
        )

        db.session.add(agendamento)
        db.session.commit()

        logger.info(f"Agendamento criado: {agendamento}")

        # Convertendo o horário para string no schema de resposta
        response_data = PostAgendamento(**data).dict()
        response_data['horario'] = str(response_data['horario'])  # Convertendo aqui, caso necessário
        
        return jsonify(response_data), 201

    except Exception as e:
        logger.error(f"Erro ao criar agendamento: {str(e)}")
        return jsonify({"error": "Erro interno"}), 500


@app.get("/agendamentos")
def get_all_agendamentos():
    """
    Retorna todos os agendamentos cadastrados no sistema.

    Retorna uma lista de agendamentos com os seguintes campos:
    - id: Identificador do agendamento.
    - data: Data do agendamento.
    - horario: Horário do agendamento.
    - cliente: Nome do cliente.
    - servico: Serviço solicitado.

    Returns:
        Response: A resposta HTTP contendo a lista de agendamentos ou um erro.
    """
    try:
        agendamentos = Agendamento.query.all()
        response = GetAllAgendamentos(
            agendamento=[
                ItemAgendamento(
                    id=str(ag.id),  # Converte o UUID para string
                    data=str(ag.data),  # Converte a data de datetime.date para string
                    horario=str(ag.horario),  # Converte o horário para string
                    cliente=ag.cliente,
                    servico=ag.servico
                ) for ag in agendamentos
            ]
        )
        return jsonify(response.dict()), 200

    except Exception as e:
        logger.error(f"Erro ao obter agendamentos: {str(e)}")
        return jsonify({"error": "Erro interno"}), 500
    

@app.get("/agendamentos/<uuid:agendamento_id>")
def get_agendamento(agendamento_id):
    """
    Retorna os detalhes de um agendamento específico pelo seu ID.

    Args:
        agendamento_id (uuid): Identificador único do agendamento.

    Retorna:
        Response: A resposta HTTP contendo os detalhes do agendamento ou um erro.
    """
    try:
        agendamento = Agendamento.query.get(agendamento_id)
        
        if not agendamento:
            return jsonify({"error": "Agendamento não encontrado"}), 404
        
        # Convertendo os tipos para strings antes de passar para o Pydantic
        response = GetByIdAgendamentos(
            id=str(agendamento.id),  # Converte UUID para string
            data=agendamento.data.strftime('%Y-%m-%d'),  # Converte date para string
            horario=agendamento.horario.strftime('%H:%M:%S'),  # Converte time para string
            cliente=agendamento.cliente,
            servico=agendamento.servico
        )
        return jsonify(response.dict()), 200

    except Exception as e:
        logger.error(f"Erro ao obter agendamento: {str(e)}")
        return jsonify({"error": "Erro interno"}), 500

from uuid import UUID

@app.put("/agendamentos/<uuid:agendamento_id>")
def update_agendamento(agendamento_id):
    """
    Atualiza os dados de um agendamento existente.

    Args:
        agendamento_id (uuid): Identificador único do agendamento a ser atualizado.

    Espera os seguintes dados no corpo da requisição:
    - data: Data do agendamento (opcional).
    - horario: Horário do agendamento (opcional).
    - cliente: Nome do cliente (opcional).
    - servico: Serviço solicitado (opcional).

    Retorna o agendamento atualizado em formato JSON.

    Returns:
        Response: A resposta HTTP com o agendamento atualizado ou um erro.
    """
    try:
        agendamento = db.session.get(Agendamento, agendamento_id)
        if not agendamento:
            return jsonify({"error": "Agendamento não encontrado"}), 404

        data = UpdateAgendamento(**request.get_json())

        if data.data is not None:
            agendamento.data = datetime.strptime(data.data, "%Y-%m-%d").date()
        if data.horario is not None:
            agendamento.horario = datetime.strptime(data.horario, "%H:%M:%S").time()
        if data.cliente is not None:
            agendamento.cliente = data.cliente
        if data.servico is not None:
            agendamento.servico = data.servico

        db.session.commit()

        return jsonify({
            "id": str(agendamento.id),
            "data": agendamento.data.strftime('%Y-%m-%d'),
            "horario": agendamento.horario.strftime('%H:%M:%S'),
            "cliente": agendamento.cliente,
            "servico": agendamento.servico
        }), 200

    except ValueError as ve:
        db.session.rollback()
        logger.error(f"Erro de validação nos dados: {str(ve)}")
        return jsonify({"error": "Formato de data ou horário inválido"}), 400
        
    except Exception as e:
        db.session.rollback()
        logger.error(f"Erro ao atualizar agendamento: {str(e)}")
        return jsonify({"error": "Erro interno do servidor"}), 500

    
@app.delete("/agendamentos/<uuid:agendamento_id>")
def delete_agendamento(agendamento_id):
    """
    Exclui um agendamento do sistema.

    Args:
        agendamento_id (uuid): Identificador único do agendamento a ser excluído.

    Retorna:
        Response: A resposta HTTP indicando o sucesso ou erro da exclusão.
    """
    try:
        agendamento = Agendamento.query.get(agendamento_id)

        if not agendamento:
            return jsonify({"error": "Agendamento não encontrado"}), 404

        db.session.delete(agendamento)
        db.session.commit()

        logger.info(f"Agendamento deletado: ID {agendamento_id}")
        return jsonify(DeleteAgendamento(id=str(agendamento_id)).dict()), 200

    except Exception as e:
        logger.error(f"Erro ao deletar agendamento: {str(e)}")
        return jsonify({"error": "Erro interno"}), 500
