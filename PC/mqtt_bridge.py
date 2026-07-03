import paho.mqtt.client as mqtt
import serial
import sys

# Configuración MQTT
BROKER    = "broker.emqx.io"
PORT      = 1883
TOPICS    = ["iot/led1", "iot/led2"]
KEEPALIVE = 60

# Configuración serial (cambia según tu sistema)
SERIAL_PORT = "COM6"   # En Windows; en Linux suele ser /dev/ttyUSB0
BAUDRATE    = 115200

try:
    ser = serial.Serial(SERIAL_PORT, BAUDRATE, timeout=5)
    print(f"Puerto serial {ser.name} abierto correctamente")
except Exception as e:
    print(f"Error al abrir el puerto serial: {e}")
    sys.exit(1)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Conectado al broker {BROKER}:{PORT} exitosamente")
        for topic in TOPICS:
            client.subscribe(topic)
            print(f"Suscrito al topic '{topic}'")
    else:
        print(f"Error de conexión. Código: {rc}")

def on_message(client, userdata, msg):
    topic   = msg.topic
    payload = msg.payload.decode("utf-8").strip()
    print(f"Topic: {topic} | Mensaje: {payload}")

    # Construir comando para el ESP32
    if topic == "iot/led1":
        comando = f"LED1:{payload}\n"
    elif topic == "iot/led2":
        comando = f"LED2:{payload}\n"
    else:
        return

    try:
        ser.write(comando.encode("utf-8"))
        print(f"Enviado por serial: {comando.strip()}")
    except Exception as e:
        print(f"Error al enviar por serial: {e}")

cliente = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
cliente.on_connect = on_connect
cliente.on_message = on_message

try:
    cliente.connect(BROKER, PORT, KEEPALIVE)
except Exception as e:
    print(f"No se pudo conectar al broker: {e}")
    sys.exit(1)

print("Esperando mensajes... (presiona Ctrl+C para salir)")

try:
    cliente.loop_forever()
except KeyboardInterrupt:
    print("\nPrograma terminado por el usuario")
    ser.close()
    cliente.disconnect()
