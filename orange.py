import RPi.GPIO as GPIO
import time

#Configuracio de pins
GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER = 23
GPIO_ECHO = 24
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def calculate_distance():
    #Enviar puls per poder medir la distància
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.000001)
    GPIO.output(GPIO_TRIGGER, False)

    #Mesurar temps de resposta
    star_time = time.time()
    while GPIO.input(GPIO_ECHO) == 0:
        star_time = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
        end_time = time.time()

    #Calcula la duracio del puls
    duration = end_time - star_time

    #Calcula la distancia, la velocitat del soroll es 343 m/s
    distance = duration * 34300 / 2

    return distance

try:
    while True:
        if distance == 0:
            distance = calculate_distance()
        else:
            new_distance = calculate_distance()
            if new_distance != distance:
                print("Ha entrat un intrus!")

except KeyboardInterrupt:
    print("Programa interroput per l'usuari")
    GPIO.cleanup()
