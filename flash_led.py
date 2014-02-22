# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)  # p7
GPIO.setup(11, GPIO.OUT)  # p0
GPIO.setup(13, GPIO.OUT)  # p2
GPIO.setup(15, GPIO.OUT)  # p3
GPIO.setup(12, GPIO.OUT)  # p1
GPIO.setup(16, GPIO.OUT)   # p4
GPIO.setup(18, GPIO.OUT)    # p5
GPIO.setup(22, GPIO.OUT)    # p6

GPIO.setup(23, GPIO.IN)    # clk

scl = 0

GPIO.output(11, True)
GPIO.output(12, True)
GPIO.output(13, True)
GPIO.output(15, True)
GPIO.output(16, True)
GPIO.output(18, True)
GPIO.output(22, True)
GPIO.output(7, True)


while True:
			scl = GPIO.input(23)
                        print "SCL={}".format(scl)
                        (time.sleep(0.2))
"""
                        GPIO.output(11, False)	
                        (time.sleep(0.2))
                        GPIO.output(11, True)
		        GPIO.output(12, False) 
                        (time.sleep(0.2))
                        
                        GPIO.output(12, True)
                        GPIO.output(13, False)
                        (time.sleep(0.2))

                        GPIO.output(13, True)
                        GPIO.output(15, False)
                        (time.sleep(0.2))

                        GPIO.output(15, True)
                        GPIO.output(16, False)
                        (time.sleep(0.2))

                        GPIO.output(16, True)
                        GPIO.output(18, False)
                        (time.sleep(0.2))

                        GPIO.output(18, True)
                        GPIO.output(22, False)
                        (time.sleep(0.2))

                        GPIO.output(22, True)
                        GPIO.output(7, False)
                        (time.sleep(0.2))

                        GPIO.output(7, True)


"""

GPIO.cleanup()

