from flask import Flask
from logger.logging import AppLogger
from flask import Flask
from models.agendamentoModels import db  
from flask_cors import CORS


logger = AppLogger().get_logger()

def create_app() -> Flask:
    app = Flask(__name__)
    CORS(app) 

    # Configuração do banco de dados
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:senha@db/agendamento"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    # Registra o app com o SQLAlchemy
    db.init_app(app)
    
    with app.app_context():
        db.create_all()  # Cria as tabelas se necessário
    
    # Configuração das rotas e Blueprints
    try:
        from routes import controller as agendamento_route  # Importa a rota de agendamento
        app.register_blueprint(agendamento_route.app)
        logger.info("Rotas configuradas com sucesso.")
    except ImportError as e:
        logger.error(f"Erro ao importar rotas: {e}")
        raise e

    return app
