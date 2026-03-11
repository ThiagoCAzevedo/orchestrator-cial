from pydantic_settings import BaseSettings
from pydantic import Field
import threading

RUNNER_LOCK = threading.Lock()
RUNNER_STOP = threading.Event()

class Settings(BaseSettings):
    # -- APP CONFIG --
    APP_NAME: str
    APP_URL: str
    FILES_DRIVER: str

    # -- MQTT CONFIG --
    AL_MQTT_ENDPOINT: str
    AL_MQTT_HOST: str
    AL_MQTT_PORT: int
    AL_MQTT_SUBSCRIBE_TOPIC: str
    AL_MQTT_PATH:str

    # -- CORE CONFIG --
    CORE_URL: str

    class Config:
        env_file = "config/.env"
        extra = "forbid"
        case_sensitive = True


settings = Settings()