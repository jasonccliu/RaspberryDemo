#!/usr/bin/python
import sys
import Adafruit_DHT
import time

while True:
    # Sensor value mapping: 11 - DHT-11 ;  22 - DHT-22
    # GPIO Connect: 4 - GPIO04 (Pin#07)
    humidity, templature = Adafruit_DHT.read_retry(22,4)
    print 'Temp: {0:0.1f} C Humidity: {1:0.1f} %'.format(templature, humidity)
    time.sleep(2)