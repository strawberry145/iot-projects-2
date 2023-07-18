import paho.mqtt.client as mqtt 
import RPi.GPIO as GPIO
import time

motion_pin = 16  #Den Pin des Bewegungssensors einer Variable zuweisen.

GPIO.setmode(GPIO.BOARD) #Die GPIO Boardkonfiguration benutzen.
GPIO.setup(motion_pin, GPIO.IN)  #Der Pin der Deklarierten Variable wird als Input gesetzt.

mqttBroker ="test.mosquitto.org" 

client = mqtt.Client("Client007")
client.connect(mqttBroker) 
  
try:                        # Beginn einer Schleife
    while True:             
       if(GPIO.input(motion_pin) == 0): # Wenn der Sensor Input = 0 ist
             print ("Sent message No motion ...") # Wird der print Befehl ausgeführt
             client.publish("smarthome/room1", "no_motion")
       elif(GPIO.input(motion_pin) == 1): # Wenn der Sensor Input = 1 ist
             print ("Sent message Motion!")  # Wird der print Befehl ausgeführt
             client.publish("smarthome/room1", "motion")
       time.sleep(0.8) # 0,1 Sekunde Warten
       
except KeyboardInterrupt:
    GPIO.cleanup()     # Gibt GPIO Ports wieder frei.
    

