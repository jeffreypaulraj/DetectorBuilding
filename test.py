import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
import RPi.GPIO as GPIO
from adafruit_mcp3xxx.analog_in import AnalogIn

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D4)
mcp = MCP.MCP3008(spi, cs)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

#pin 18 is red
#pin 23 is green 
#pin 24 is blue 

a = 3

channel = AnalogIn(mcp, MCP.P0)

while True:
        print('Raw ADC Value: ', channel.value)
        print('ADC Voltage: ' + str(channel.voltage) + 'V') 
        
        temp = (37.6 * channel.voltage) - 37.4
        print('Temp: ' + temp + 'C')
        
        time.sleep(0.5)
        if(a == 1):
                GPIO.output(18, GPIO.HIGH)
        if(a == 2):
                GPIO.output(23, GPIO.HIGH)
        if(a == 3):
                GPIO.output(24, GPIO.HIGH)



