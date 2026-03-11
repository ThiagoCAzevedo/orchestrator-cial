from fastapi import APIRouter
from modules.mqtt_listener.listener import MQTTOrchestrator
from common.logger import logger


router = APIRouter()
mqtt = MQTTOrchestrator()
started = False


@router.post("/mqtt/start")
def start_mqtt():
    if started:
        logger.info("MQTT is already running")
        return {"status": "already_running"}

    mqtt.connect()
    mqtt.start()
    started = True

    logger.info("MQTT started successfully")
    return {"status": "started"}

@router.post("/mqtt/stop")
def stop_mqtt():
    if not started:
        logger.info("MQTT is not running")
        return {"status": "not_running"}

    mqtt.stop()
    started = False

    logger.info("MQTT stopped successfully")
    return {"status": "stopped"}