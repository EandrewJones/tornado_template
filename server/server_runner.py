import asyncio

import tornado.ioloop

from server.endpoints import App
from src.utils.log_handler import LogHandler

log_handler = LogHandler(__name__)


def run_server(server_port: int):
    # Create the event loop spawning up the tornado server
    asyncio.set_event_loop(asyncio.new_event_loop())

    server_app = App()
    server_app.listen(server_port)

    # Start the server loop
    try:
        log_handler.log_info(f"Server started on port {server_port}...")
        tornado.ioloop.IOLoop.current().start()
    except Exception as e:
        log_handler.log_exceptions(str(e))
