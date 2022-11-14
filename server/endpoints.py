import tornado.web

from config import Config
from handlers.health_check_handler import HealthCheckHandler


class App(tornado.web.Application):
    def __init__(self):
        # Define the handlers answering requests from clients
        self.endpoint_version_prefix = f"/api/{Config.API_VERSION}"
        self.handlers = [
            (self.endpoint_version_prefix + r"/_health", HealthCheckHandler),
        ]
        super(App, self).__init__(self.handlers)
