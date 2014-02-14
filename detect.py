# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
from subprocess import call
from time import sleep


GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)
GPIO.setup(7, GPIO.OUT)

image_count = 1
video_count = 1

a = 0
count = 0
state1 = 0

while True:
	state1 = a
	a = GPIO.input(12)

	if state1 != a:
		if a > 0:
			GPIO.output(7, False)	
			print("Движение...... image%s.jpg\n" % image_count)
                        strImage = str(image_count)
                        call (["raspistill -t 1000   -o images/image" + strImage + ".jpg"], shell=True)
                        image_count = image_count + 1                                    

                        strVideo = str(video_count)
                        call (["raspivid -t 5000   -o video/video" + strVideo + ".avi"], shell=True)
                        video_count = video_count + 1

		elif a < 1:
			GPIO.output(7, True)
			print("Ожидание..\n")

GPIO.cleanup()

