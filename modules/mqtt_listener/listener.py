from config.settings import settings, RUNNER_STOP, RUNNER_LOCK
from modules.pipeline.runner import runner
import paho.mqtt.client as mqtt
import threading


class MQTTOrchestrator:
    def __init__(self):
        self.host = settings.AL_MQTT_HOST
        self.port = settings.AL_MQTT_PORT
        self.ws_path = settings.AL_MQTT_PATH

        self.client = mqtt.Client(protocol=mqtt.MQTTv311, transport="websockets")
        self.client.tls_set(cert_reqs=False)
        self.client.tls_insecure_set(True)
        self.client.ws_set_options(path=self.ws_path)

        self.client.on_message = self._on_message

    def _on_message(self, client, userdata, msg):
        if RUNNER_LOCK.locked():
            return
        
        def _run():
            with RUNNER_LOCK:
                RUNNER_STOP.clear()
                runner()

        threading.Thread(target=_run, daemon=True).start()

    def connect(self):
        self.client.connect(self.host, self.port)
        self.client.subscribe(settings.AL_MQTT_SUBSCRIBE_TOPIC)

    def start(self):
        RUNNER_STOP.clear()
        self.client.loop_start()

    def stop(self):
        RUNNER_STOP.set()
        self.client.loop_stop()
        self.client.disconnect()