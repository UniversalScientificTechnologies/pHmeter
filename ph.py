#!/usr/bin/python
import time
import sys
from pymlab import config

from pylab import *
import time
import numpy as np

color = ['\33[0m','\33[91m','\33[92m','\33[93m','\33[94m','\33[95m','\33[96m']

while True:
    #### Sensor Configuration ###########################################
    cfg = config.Config(
        i2c =
		{
            "port": 1, # I2C bus number
        },

	    bus = 
		[
        	{
                "type": "i2chub",
                "address": 0x73, #0x72
                
                "children": 
				[
                    {"name": "adc1", "type": "i2cadc01" , "channel": 1, },   
                    {"name": "adc2", "type": "i2cadc01" , "channel": 2, },   
                    {"name": "adc3", "type": "i2cadc01" , "channel": 3, },   
                    {"name": "adc4", "type": "i2cadc01" , "channel": 4, },   
                    {"name": "adc5", "type": "i2cadc01" , "channel": 5, },   
                    {"name": "adc6", "type": "i2cadc01" , "channel": 6, },   
				],
			},
		],
    )

    cfg.initialize()
    adc = [0,cfg.get_device("adc1"),cfg.get_device("adc2"),cfg.get_device("adc3"),cfg.get_device("adc4"),cfg.get_device("adc5"),cfg.get_device("adc6")]

    time.sleep(0.5)

    try:
        while True:
			for n in range(1,7):
				adc[n].route()
				if n==1:
					# Temperature readout
					temperature = adc[n].readTemp()
					temperature += 7
					print "T","{:+5.1f}".format(temperature),
					print " pH",
				#time.sleep(1)
				# Voltage readout
				voltage = adc[n].readADC()
				ph = -(voltage / 0.050) + 7   #pH
				print color[n], "{:5.2f}".format(ph),
				#time.sleep(1)
			print color[0]

        print "IOError"
        continue

    except KeyboardInterrupt:
    	sys.exit(0)


