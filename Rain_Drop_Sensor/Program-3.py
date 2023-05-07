#https://github.com/thyagarajank/Raspberry-Pi-IoT-Sensors-Program
# raindrop sensor DO connected to GPIO18
# HIGH = no rain, LOW = rain detected
from time import sleep
from gpiozero import Buzzer, InputDevice
 
buzz    = Buzzer(13)
no_rain = InputDevice(23)
 
def buzz_now(iterations):
    for x in range(iterations):
        buzz.on()
        sleep(0.1)
        buzz.off()
        sleep(0.1)

print "Initialzing Rain Drop Sensor......"
sleep(1)
print "Measure time & analysis..."

while True:
    if not no_rain.is_active:
        print("Rain Drop detected!")
        buzz_now(5)
        # insert your other code or functions here
        # e.g. tweet, SMS, email, take a photo etc.
    sleep(1)

