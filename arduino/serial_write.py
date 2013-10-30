#!/usr/bin/env python

import serial

ser = serial.Serial("/dev/ttyUSB0", 9600)
ser.write('1')
ser.close()
