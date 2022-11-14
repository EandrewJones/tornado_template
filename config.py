import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # Tornado Server Vars
    API_VERSION = os.getenv("API_VERSION") or "v1"
    SERVER_PORT = int(os.getenv("SERVER_PORT")) or 8000
    SERVICE_TOKEN = os.getenv("SERVICE_TOKEN")
    REQUEST_CTR_LIMIT = 4  # Max retries for external service calls
    REQUEST_SLEEP_TIME = 45  # Default sleep time
    WEBHOOK_URL = (
        os.getenv("WEBHOOK_URL") or None
    )  # An optional webhook URL to log exceptions to

    # Add additional parameters below
