#https://github.com/thyagarajank/Raspberry-Pi-IoT-Sensors-Program
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(40, GPIO.IN) #PIR

print "Initialzing PIR Sensor......"
time.sleep(1)
print "PIR Ready..."
print " Scanning..."


try:
    #time.sleep(1) # to stabilize sensor
    while True:
	time.sleep(2)
        if(GPIO.input(40)==1):
            print("Objects Motion Detected...")
           # time.sleep(2) #to avoid multiple detection
        #time.sleep(0.1) #loop delay, should be less than detection delay
	else:
	    print("NO Objects Detect")
	    
except:
    GPIO.cleanup()

