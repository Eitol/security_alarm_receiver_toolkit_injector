import RPi.GPIO as GPIO
import time

LedBLUE = 19  # pin11
LedRED = 21  # pin11


def setup():
    GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
    GPIO.setup(LedBLUE, GPIO.OUT)  # Set LedBLUE's mode is output
    GPIO.output(LedBLUE, GPIO.HIGH)  # Set LedBLUE high(+3.3V) to turn on led
    GPIO.setup(LedRED, GPIO.OUT)  # Set LedBLUE's mode is output
    GPIO.output(LedRED, GPIO.HIGH)  # Set LedBLUE high(+3.3V) to turn on led


def blink():
    while True:
        # Only RED
        GPIO.output(LedRED, GPIO.HIGH)  # led on
        time.sleep(1)
        GPIO.output(LedRED, GPIO.LOW)  # led on
        time.sleep(1)

        # Only BLUE
        GPIO.output(LedBLUE, GPIO.HIGH)  # led on
        time.sleep(1)
        GPIO.output(LedBLUE, GPIO.LOW)  # led on
        time.sleep(1)

        # RED+BLUE = Magenta
        GPIO.output(LedRED, GPIO.HIGH)  # led on
        GPIO.output(LedBLUE, GPIO.HIGH)  # led on
        time.sleep(1)
        GPIO.output(LedRED, GPIO.LOW)  # led on
        GPIO.output(LedBLUE, GPIO.LOW)  # led on
        time.sleep(1)


def destroy():
    GPIO.output(LedBLUE, GPIO.LOW)  # led off
    GPIO.output(LedRED, GPIO.LOW)  # led off
    GPIO.cleanup()  # Release resource


if __name__ == '__main__':  # Program start from here
    setup()
    try:
        blink()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()