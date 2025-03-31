from logger.logging import AppLogger 
from app_factory import create_app
from config import Config

logger = AppLogger().get_logger()


app = create_app()

app.run(host=Config.HOST, port=Config.PORT)
    
    
    