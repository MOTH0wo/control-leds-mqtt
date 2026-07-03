from machine import Pin, UART
import sys

led1 = Pin(13, Pin.OUT)
led2 = Pin(12, Pin.OUT)
uart = sys.stdin.buffer 

print("ESP32 lista, esperando comandos...")

while True:
    linea = sys.stdin.readline().strip()
    if not linea:
        continue

    print(f"Recibido: {linea}")

    if linea == "LED1:1":
        led1.value(1)
        print("LED1 encendido")
    elif linea == "LED1:0":
        led1.value(0)
        print("LED1 apagado")
    elif linea == "LED2:1":
        led2.value(1)
        print("LED2 encendido")
    elif linea == "LED2:0":
        led2.value(0)
        print("LED2 apagado")
