import RPi.GPIO as GPIO
from time import sleep


def safeCleanUp():
    ''' Clean up script for GPIO pins '''
    try:
        # Try cleaning up any remaining GPIO channels, if they exist
        GPIO.cleanup()
    except RuntimeWarning:
        pass



def servoController(motorGPIOs, pwmArray, direction='CW', update_frequency=0.1, verbose=False):

    ''' Powers a motor via GPIO pins in the specified direction (CW or CCW)
    given an array of PWM values (having a range 0-100). For RPi3 typical GPIO
    pinout is [16,18,22]. Update frequency tells how many seconds the script
    should wait before updating the motor's output GPIO.
    '''

    if verbose:
        print('Setting up GPIO pins...')
        
    GPIO.setmode(GPIO.BOARD)
    MotorA,MotorB,MotorE = motorGPIOs

    # Looping through the GPIO pins used for this motor and activating them as output GPIOs
    for GPIO_pin in motorGPIOs:
        GPIO.setup(GPIO_pin, GPIO.OUT)

    if direction=='CCW':
        GPIO.output(MotorA, GPIO.LOW)
        GPIO.output(MotorB, GPIO.HIGH)
        if verbose:
            print('Engaging motor in CCW direction.')
    if direction=='CW':
        GPIO.output(MotorA, GPIO.HIGH)
        GPIO.output(MotorB, GPIO.LOW)
        if verbose:
            print('Engaging motor in CW direction.')

    pwm=GPIO.PWM(MotorE,100)
    pwm.start(pwmArray[0])

    if verbose:
        print('Engaging PWM array sequence.')

    for pwm_value in pwmArray:
        try:  
            pwm.ChangeDutyCycle(pwm_value)
        except ValueError:
            if verbose:
                print('Value Error encountered... defaulting to last possible value')
                print('Check bounds of input PWM (0-100)')
            pass
        sleep(update_frequency)

    if verbose:
        print('Turning off motor.')
        
    GPIO.output(MotorE, GPIO.LOW)

    return


