# Control de LEDs mediante MQTT

Sistema IoT que permite controlar dos LEDs conectados a un ESP32 a través de una interfaz web y un puente MQTT-Serial.

# Características

- Interfaz web sencilla con botones para encender/apagar cada LED.
- Comunicación MQTT mediante broker público (EMQX).
- Puente MQTT-Serial en Python que traduce mensajes a comandos para el ESP32.
- Código para ESP32 en MicroPython.

# Tecnologías utilizadas

- **Python 3** + `paho-mqtt` + `pyserial`
- **MicroPython** en ESP32
- **HTML/CSS/JS** (frontend)
- **MQTT** (broker EMQX)

#Notas importantes

- **El broker EMQX es público y gratuito, ideal para pruebas. Para producción, usa tu propio broker.**
- **Pines del ESP32: Modifica las líneas led1 = Pin(13, Pin.OUT) y led2 = Pin(12, Pin.OUT) según tus necesidades o puedes agregar mas eso implicaria cambiar el html.**
- **La comunicación serial asume que el ESP32 está conectado por USB y se comunica a través de sys.stdin/sys.stdout.**

🤝 Contribuciones

Si encuentras algún problema o quieres mejorar el proyecto, no dudes en abrir un issue o un pull request.
