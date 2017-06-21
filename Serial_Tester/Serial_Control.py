# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 21:45:19 2017

@author: Jeff Beckman
"""

import serial
import time

ser = serial.Serial('COM4', 9600, timeout = 0)

while True:
    try:
        print(ser.readline())
        time.sleep(1)
    except ser.SerialTimeoutException:
        print("Data could not be read")
        time.sleep(1)