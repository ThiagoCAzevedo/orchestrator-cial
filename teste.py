import json
import paho.mqtt.client as mqtt

last_value = None  # guarda o último valor recebido

def on_message(client, userdata, msg):
    global last_value

    payload = msg.payload.decode("utf-8")

    try:
        data = json.loads(payload)   # tenta ler como JSON
    except:
        data = payload               # senão usa como string normal

    # Detecta mudança
    if last_value is None:
        print("Primeira leitura — sem comparação.")
    elif data != last_value:
        print("🔄 MUDOU! Novo valor:", data)   # << só mostra o valor novo
    else:
        print("✔️ NÃO MUDOU.")

    last_value = data  # atualiza o valor anterior


# ==============================
# MQTT via WebSocket seguro (WSS)
# ==============================

client = mqtt.Client(protocol=mqtt.MQTTv311, transport="websockets")

client.tls_set(cert_reqs=False)
client.tls_insecure_set(True)

client.ws_set_options(path="/v1/mqtt")

client.on_message = on_message

client.connect("10.135.121.158", 40520)
client.subscribe("#")

print("Orquestrador iniciado... aguardando mensagens.\n")

client.loop_forever()