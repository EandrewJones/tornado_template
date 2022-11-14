from app.server.server_runner import run_server
from app.src.utils.log_handler import LogHandler
from config import Config

log_handler = LogHandler(__name__)


if __name__ == "__main__":
    run_server(Config.SERVER_PORT)
