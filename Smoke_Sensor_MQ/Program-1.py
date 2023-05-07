#https://github.com/thyagarajank/Raspberry-Pi-IoT-Sensors-Program
/* MQ Smoke Sensor  Raspberry Pi */

import time
import botbook_mcp3002 as mcp 

smokeLevel= 0

def readSmokeLevel():
global smokeLevel
smokeLevel= mcp.readAnalog()

def main():
while True: 
readSmokeLevel() 
print ("Current smoke level is %i " % smokeLevel) 
if smokeLevel > 120:
print("Smoke detected")
time.sleep(0.5) 

if_name_=="_main_":
main()
