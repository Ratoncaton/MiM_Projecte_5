import Adafruit_DHT
import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont

#Iniciar la pantalla
RST = None

disp = Adafruit_SSD1306.SSD1306_128_64(RST)

disp.begin()
disp.clear()
disp.display()

#Crear imatge a la pantalla per poder escriure
width = disp.width
height = disp.height
image = Image.new("1", (width, height))
draw = ImageDraw.Draw(image)

#Identificar els sensors d'humitat i temperatura
SENSOR_DHT = Adafruit_DHT.DHT11
PIN_DHT = 4

while True:
    humedad, temperatura = Adafruit_DHT.read(SENSOR_DHT, PIN_DHT)
    if humedad is not None and temperatura is not None:
        #Borra pantalla
        draw.rectangle((0,0, width, height), outline=0, fill=0)
        #Missatge
        message = "Temperatura={0:01f}C Humetat={1:0.1f}%".format(temperatura,humetat)
        #Preparar el missatge
        draw.text((0,0), message, font=font, fill=255)
        #Mostrar la imatge
        disp.image(image)
        disp.display()

