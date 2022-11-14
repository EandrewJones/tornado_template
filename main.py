from config import Config
from server.server_runner import run_server
from src.utils.log_handler import LogHandler

log_handler = LogHandler(__name__)


if __name__ == "__main__":
    run_server(Config.SERVER_PORT)
