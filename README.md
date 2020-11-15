# Temperature-Monitoring-System
The temperature monitoring system is an embedded system utilizing Raspberry Pi and a GrovePi HAT along with a temperature sensor, humidity sensor, LCD screen, 3 LED lights and a light sensor. The program was developed using Python. The device records room temperature and humidity every 30 minutes only during day light hours based on the light sensor conditions. The current temperature and humidity is displayed on the LCD screen. The program contains conditional statements that once a specified temperature or humidity is reached the LED will light up to give the user a visual indication of temperature and humidity. For example, when the red LED lights up that means it is too hot and to humid for room conditions. Every 30 minutes the current reading is written to a JSON file that is used to display that data in CanvasJS. 
