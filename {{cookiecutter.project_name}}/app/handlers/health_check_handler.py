from app.handlers.base_handler import BaseHandler
from app.src.utils.log_handler import LogHandler

log_handler = LogHandler(__name__)


class HealthCheckHandler(BaseHandler):
    def get(self):
        headers = self.request.headers
        try:
            token_str = headers.get("Authorization")
            if "Bearer" not in token_str:
                return self.reply_client(
                    status_code=400, data={"msg": "authentication header is malformed."}
                )
            token = token_str.split(" ")[1]
            if self.validate_token(token) is not True:
                return self.reply_client(
                    status_code=401, data={"msg": "invalid credentials"}
                )
        except Exception as e:
            log_handler.log_exceptions(exception=str(e))
            return self.reply_client(status_code=400, data={"msg": "bad request"})

        return self.reply_client(status_code=200, data={"msg": "ok"})
