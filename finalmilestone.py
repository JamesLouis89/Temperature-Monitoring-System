#!/usr/bin/python3


import datetime
import time
import json
import math
import time
from grove_rgb_lcd import*
from grovepi import *

###****Setting D-Ports for Led Lights
greenled = 3
redled = 5
blueled = 6

##****weather sensor type and location on d5*****####
weatherSensor = 4
blue = 0

##****setting analog port for light sensor and threshold to monitor day or night****###
light_sensor = 0
lightSensorThreshold = 10
##****setting input and output
pinMode(light_sensor,"INPUT")
##pinMode(weatherSensor,"INPUT")
pinMode(greenled,"OUTPUT")
pinMode(redled,"OUTPUT")
pinMode(blueled,"OUTPUT")



##***Creating file path and list format for writing to JSON file*****####

path = '/home/pi/Documents'
FileName = 'FinalReadings'
ext = '.json'

filePathAndExt = path + FileName + ext

data ={}
data['reading'] = []

while True:
    try:
        sensor_value = analogRead(light_sensor)
        resistance = (float)(1023 - sensor_value) * 10 / sensor_value
      
        

        ##***We will first get the weather and temp to only record during the day***###
        if resistance > lightSensorThreshold:
            now = datetime.datetime.now() #used a time stamp to show it was recording every 30 minutes
            [temp,humidity] = dht(weatherSensor,blue)
            temp = ((temp * 9) / 5.0) + 32 ##***convets to farenheit**##
            
            ###Below creates a list that is written to the json file
            data['reading'].append([temp,
                                    humidity])
            with open(filePathAndExt,'w') as fp:
                json.dump(data['reading'], fp, indent=3)
            print("temp = %.02f C humidity =%.02f%%"%(temp, humidity) + now.strftime(" %H:%M:%S"))
            ###conditional statements for when the led will light up 
            if( temp > 60 and temp < 80 and humidity < 80):
                digitalWrite(greenled,1)
            

            elif( temp > 85 and temp < 95 and humidity < 80):
                digitalWrite(blueled, 1)

            elif( temp > 95):
                digitalWrite(redled,1)
            

            elif( humidity > 90):
                digitalWrite(greenled, 1)
                digitalWrite(blueled, 1)

            ##shuts off led if a different condition is met
            else:
                digitalWrite(greenled,0)
                digitalWrite(blueled,0)
                digitalWrite(redled,0)
        else:
            print("Not correct")
             
        time.sleep(1800)####Records temp and humidity every 30 minutes

        ##puts the temp and humidity into a string to be printed on the LCD
        t = str(temp)
        h = str(humidity)

        ##Sets the color, the text and I added a timer for every 3 seconds to record temp
        setRGB(400,10,10)
        setText_norefresh("Temp:" + t + "F" + "\n" + "Humidity:" + h + "%")


    
    except KeyboardInterrupt: ## shuts off LED by using ctrl + c
        digitalWrite(greenled,0)
        digitalWrite(blueled,0)
        digitalWrite(redled,0)
        break
            
            
    except IOError:
        print("Error")
                
            
            
            
        



