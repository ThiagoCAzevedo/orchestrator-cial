from config.settings import settings
import paho.mqtt.client as mqtt


class MQTTOrchestrator:
    def __init__(self):
        self.host = settings.AL_MQTT_IP
        self.port = settings.AL_MQTT_PORT
        self.ws_path = settings.AL_MQTT_PATH

        self.client = mqtt.Client(protocol=mqtt.MQTTv311, transport="websockets")

        self.client.tls_set(cert_reqs=False)
        self.client.tls_insecure_set(True)

        self.client.ws_set_options(path=self.ws_path)

        self.client.on_message = self._on_message

    def _on_message(self, client, userdata, msg):
        # call core pipeline
        pass 

    def connect(self):
        self.client.connect(self.host, self.port)
        self.client.subscribe(settings.AL_MQTT_SUBSCRIBE_TOPIC)

    def start(self):
        self.client.loop_forever()