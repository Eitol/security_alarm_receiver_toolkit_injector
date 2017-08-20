import socketio
from serial import Serial
import RPi.GPIO as GPIO
import time

sio = socketio.AsyncServer()
# Serial port for raspberry pi 3
SERIAL_PORT = '/dev/ttyS0'
dev = Serial(SERIAL_PORT, 9600, timeout=0.5)
LedBLUE = 19  # pin11
LedRED = 21  # pin11


def serial_setup():
    GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
    GPIO.setup(LedBLUE, GPIO.OUT)  # Set LedBLUE's mode is output
    GPIO.output(LedBLUE, GPIO.LOW)  # Set LedBLUE high(+3.3V) to turn on led
    GPIO.setup(LedRED, GPIO.OUT)  # Set LedBLUE's mode is output
    GPIO.output(LedRED, GPIO.LOW)  # Set LedBLUE high(+3.3V) to turn on led


@sio.on('connect')
def connect(sid, environ):
    print("connect ", sid)


@sio.on('send signal')
async def message(sid, data):
    print("message ", data)
    dev.write(data.encode())
    GPIO.output(LedBLUE, GPIO.HIGH)  # led on
    time.sleep(1)
    GPIO.output(LedBLUE, GPIO.LOW)  # led on
    time.sleep(1)
    await sio.emit('send signal', room=sid)


@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)