from machine import Pin, Timer
import time
import network
from umqtt.simple import MQTTClient

temporiza = Timer(0)

# MQTT Configuration
MQTT_CLIENT_ID = "alciaaaaaaaaaaaaaaaaaaaaaaaa"
MQTT_BROKER = "broker.hivemq.com"
MQTT_USER = ""
MQTT_PASSWORD = ""
topic_pub = "ALCANCIA/juan"
topic_sub = 'alcancia/juan'

#Total
total = 0
pausa = 1

#Sensores
sensor1 = Pin(27, Pin.IN, Pin.PULL_DOWN)
sensor2 = Pin(26, Pin.IN, Pin.PULL_DOWN)
sensor3 = Pin(25, Pin.IN, Pin.PULL_DOWN)
sensor4 = Pin(33, Pin.IN, Pin.PULL_DOWN)
sensor5 = Pin(32, Pin.IN, Pin.PULL_DOWN)

#Estado anterior sensores
estado_anterior1 = 0
estado_anterior2 = 0
estado_anterior3 = 0
estado_anterior4 = 0
estado_anterior5 = 0

# Connect to the internet
def conectar(red, passwd):
    global miRed

    miRed = network.WLAN(network.STA_IF)

    if not miRed.isconnected():
        miRed.active(True)
        miRed.connect(red, passwd)
        print(f'Conectando a la red {red} ...')
        timeout = time.time()

        while not miRed.isconnected():
            if (time.ticks_diff(time.time(), timeout) > 10):
                return False

    return True

#Marihuana Legal, TobyColombianoyDiosito
#Claro_64C641_EXT', 'R4Z2R7Z9R8A5'
if conectar('Claro_64C641', 'R4Z2R7Z9R8A5'):
    print('Conectado exitosamente!')
    print(f'Datos de la red (IP/Netmask/gw/DNS): {miRed.ifconfig()}')

    print("Connecting to MQTT server...", end="")

    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)
    client.connect()

    print(f"Connected to {MQTT_BROKER} MQTT broker")
    print("Connected!")

    while True:
        estado_sensor1 = sensor1.value()
        estado_sensor2 = sensor2.value()
        estado_sensor3 = sensor3.value()
        estado_sensor4 = sensor4.value()
        estado_sensor5 = sensor5.value()
        cantidad = 0
        
        if estado_sensor1 != 1:
            cantidad = 50
            total += cantidad
            client.publish("ALCANCIA/juan", str(total))
            time.sleep(1)
        if estado_sensor2 != 1:
            cantidad = 100
            total += cantidad
            client.publish("ALCANCIA/juan", str(total))
            time.sleep(1)
        if estado_sensor3 != 1:
            cantidad = 200
            total += cantidad
            client.publish("ALCANCIA/juan", str(total))
            time.sleep(1)
        if estado_sensor4 != 1:
            cantidad = 500
            total += cantidad
            client.publish("ALCANCIA/juan", str(total))
            time.sleep(1)
        if estado_sensor5 != 1:
            cantidad = 1000
            total += cantidad
            client.publish("ALCANCIA/juan", str(total))
            time.sleep(1)
else:
    print('No se pudo conectar...')
    miRed.active(False)
