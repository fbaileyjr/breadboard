# import necessary libraries
import RPi.GPIO as GPIO, time

# define a function to turn the light on then off
def blinkOnce(pin):
    GPIO.output(pin, True)
    time.sleep(1)
    GPIO.output(pin, False)
    time.sleep(1)


# initialize the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)


# use blinkOnce function in a loop
for i in range(10):
    blinkOnce(17)


# cleanup comment
GPIO.cleanup()
