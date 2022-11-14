import logging

import requests

from config import Config


class LogHandler:
    def __init__(self, name, webhook=Config.WEBHOOK_URL):
        self.name = name
        self.webhook = webhook
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

        # Setup console handler
        formatter = logging.Formatter(
            "[%(levelname)s | %(name)s][%(asctime)s.%(msecs)03d]: %(message)s",
            datefmt="%H:%M:%S",
        )
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def log_exceptions(self, exception):
        error = f"Error in generate_decision_table : {exception}"
        self.logger.error(error)
        if self.webhook:
            requests.post(self.webhook, {"content": error})

    def log_info(self, info):
        self.logger.info(info)
