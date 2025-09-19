import network
import time
import urequests
import dht
from machine import Pin

# Wi-Fi credentials
ssid = 'Wokwi-GUEST'
password = ''

# ThingSpeak API configuration
THINGSPEAK_API_KEY = '0ZGO124O16VWSK0Q'
THINGSPEAK_URL = 'https://api.thingspeak.com/update'

# Set up Wi-Fi in station mode
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# Wait until connected
print("Connecting to Wi-Fi...", end="")
while not wlan.isconnected():
    print(".", end="")
    time.sleep(0.5)

# Once connected, print confirmation and IP address
print("\nConnected!")
print("IP address:", wlan.ifconfig()[0])

# Initialize the DHT22 sensor on GPIO pin 15
sensor = dht.DHT22(Pin(15))

# Function to send temperature and humidity to ThingSpeak
def send_to_thingspeak(temp, humidity):
    if temp is None or humidity is None:
        print("No data to send.")
        return
    try:
        response = urequests.post(
            THINGSPEAK_URL,
            data='api_key={}&field1={}&field2={}'.format(THINGSPEAK_API_KEY, temp, humidity),
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
        )
        print("ThingSpeak response:", response.text)
        response.close()
    except Exception as e:
        print("Failed to send data:", e)

# Main loop: read sensor and send data every 15 seconds
while True:
    try:
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()
        print("Temperature:", temperature, "°C")
        print("Humidity:", humidity, "%")
        send_to_thingspeak(temperature, humidity)
    except Exception as e:
        print("Error reading sensor or sending data:", e)

    time.sleep(15)
