# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 21:54:02 2020

@author: Jacob
"""
import numpy as np
from motor_control import servoController, safeCleanUp


pwm_array = list(500*np.linspace(0,1)) + list(500*np.linspace(1,0))
motor_list = [16,18,22] # the + , -, and enabler GPIO pins


try:

    servoController(motor_list, pwm_array, direction='CCW')
    servoController(motor_list, pwm_array, verbose=True)
    
except KeyboardInterrupt:
    pass

safeCleanUp()
