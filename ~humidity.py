import Adafruit_DHT
import time
import matplotlib.pyplot as pp
#this code reads the temperature and humidity from raspberry pi sensor
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    
    if humidity is not None and temperature is not None:
    
        print("Temp={0:0.1f}°C Humidity={1:0.1f}%".format(temperature, humidity))
        
    else:
        print("Failed to retrieve data from humidity sensor")
    time.sleep(3600);
    

