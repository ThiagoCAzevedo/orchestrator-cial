from fastapi import APIRouter
import threading

from modules.mqtt_listener.listener import MQTTOrchestrator

router = APIRouter()

mqtt = MQTTOrchestrator()
mqtt_thread: threading.Thread | None = None


@router.post("/mqtt/start")
def start_mqtt():
    global mqtt_thread

    if mqtt_thread and mqtt_thread.is_alive():
        return {"status": "already_running"}

    mqtt.connect()
    mqtt_thread = threading.Thread(target=mqtt.start, daemon=True)
    mqtt_thread.start()

    return {"status": "started"}


@router.post("/mqtt/stop")
def stop_mqtt():
    global mqtt_thread

    if not mqtt_thread or not mqtt_thread.is_alive():
        return {"status": "not_running"}

    mqtt.stop()
    mqtt_thread = None

    return {"status": "stopped"}