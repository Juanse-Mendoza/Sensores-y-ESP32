from machine import Pin
import time
import network
import json
import urequests

# Total
total = 0

# Sensors
sensor1 = Pin(27, Pin.IN, Pin.PULL_DOWN)
sensor2 = Pin(26, Pin.IN, Pin.PULL_DOWN)
sensor3 = Pin(25, Pin.IN, Pin.PULL_DOWN)
sensor4 = Pin(33, Pin.IN, Pin.PULL_DOWN)
sensor5 = Pin(32, Pin.IN, Pin.PULL_DOWN)

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
#':D', 'e1c3cd60'
if conectar(':D', 'e1c3cd60'):
    print('Conectado exitosamente!')
    print(f'Datos de la red (IP/Netmask/gw/DNS): {miRed.ifconfig()}')
else:
    print('No se pudo conectar...')
    miRed.active(False)

url = "https://maker.ifttt.com/trigger/Notifica/with/key/lokZTHLP5nkP7aVsVQI7m7l-iMX6t1gdKSrYNMPizoB?"

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
            print("Total: " + str(total))
        if estado_sensor2 != 1:
            cantidad = 100
            total += cantidad
            print("Total: " + str(total))
        if estado_sensor3 != 1:
            cantidad = 200
            total += cantidad
            print("Total: " + str(total))
        if estado_sensor4 != 1:
            cantidad = 500
            total += cantidad
            print("Total: " + str(total))
        if estado_sensor5 != 1:
            cantidad = 1000
            total += cantidad
            print("Total: " + str(total))
        if total % 10000 == 0 and total != 0:  # Verificar si total es múltiplo de 10,000
            respuesta = urequests.get(url + "&value1=" + str(total))
            print(respuesta.text)
            print(respuesta.status_code)
            respuesta.close()


        time.sleep(1)
