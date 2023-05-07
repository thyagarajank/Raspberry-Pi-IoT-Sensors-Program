#https://github.com/thyagarajank/Raspberry-Pi-IoT-Sensors-Program
import RPi.GPIO as GPIO
import time
#import emoji 
 
#GPIO SETUP
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.IN)
GPIO.setup(7,GPIO.OUT)

print "Initialzing Moisture Sensor......"
time.sleep(1)
print "Measure Moisture Level..."

while True:
           if (GPIO.input (8)==0):
		GPIO.output(7,0)
                print "Land Moisture Level is High!!!!!"
		time.sleep(5)
		#print("\U0001f600")  
           else:
		GPIO.output(7,1)
                print "Land Misture Level is Normal"
		time.sleep(5)
		#print("\U0001f600") 


