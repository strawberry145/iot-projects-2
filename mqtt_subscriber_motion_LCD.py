import paho.mqtt.client as mqtt
import time
import board
import busio
import adafruit_character_lcd.character_lcd_i2c as character_lcd


# Definiere LCD Zeilen und Spaltenanzahl.
lcd_columns = 16
lcd_rows    = 2

# Initialisierung I2C Bus
i2c = busio.I2C(board.SCL, board.SDA)

# Festlegen des LCDs in die Variable LCD
lcd = character_lcd.Character_LCD_I2C(i2c, lcd_columns, lcd_rows, 0x21)

def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))
    lcd.clear()
    lcd.cursor = True
    lcd.message = str(message.payload.decode("utf-8"))


 #print("received message: " ,message)

mqttBroker ="test.mosquitto.org"

client = mqtt.Client("Client005")
client.connect(mqttBroker)

client.loop_start()

client.subscribe("smarthome/room1")
client.on_message=on_message

#time.sleep(30)
#client.loop_stop()