#!/usr/bin/python
# This script will read the temperature from the ADC and convert it to Farenheit.

import time
import math
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()
port = 0

# Constants
beta = 3890.0
room_temp = 298.15
max_voltage = 4.096 / 32767.0 # modify voltage based on gain level

GAIN = 1

print('Reading ADC to get temperature.')

#thermistor reading function
def temp_get(port):
    value = adc.read_adc(port, gain=GAIN) #read the adc
    voltage = (value * max_voltage)

    R = 10000.0 * ((5.18 / voltage) - 1.0)
    print "ADC: ", value, "Voltage: ", voltage, ", Resistance: ", R

    tempK = (beta * room_temp) / (beta + (room_temp * math.log(R/10000.0)))

    tempC = tempK - 273.15
    tempF = (9.0/5.0)*tempC + 32.0
    print "Temperature: ", tempF, " *F,", tempC, " *C,", tempK, " *K"
    return tempF

while True:
    temp_get(0)
    time.sleep(1)
