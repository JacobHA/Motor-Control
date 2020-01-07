## Motor-Control
Script for controlling servo motor speed and direction on RPi

Provide a direction (Clockwise=CW or Counterclockwise=CCW) as well as a speed. The list input (pwmArray) requires percentage speed (0-100). The list is iterated through and the motor speed is updated every (default update_frequency=) 0.1 seconds. 

# Dependencies
pip install RPi

I have used numpy to write the array of motor speed values.
