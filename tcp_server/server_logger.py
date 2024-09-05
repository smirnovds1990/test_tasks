import logging


server_logger = logging.getLogger(__name__)
logging.basicConfig(
    filename='server_logs.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s'
)
