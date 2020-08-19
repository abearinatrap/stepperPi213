#for use with websocket webserver
import RPi.GPIO as GPIO
import time,sys

#setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#gpio pins to control stepper motor
GPIO.setup(8, GPIO.OUT)

def setGPIO(modeN):
    GPIO.output(8,modeN)
if __name__ == "__main__":
    if sys.argv[1]=="1":
        setGPIO(GPIO.HIGH)
    elif sys.argv[1]=="0":
        setGPIO(GPIO.LOW)
    else:
        print("Bad input")
    GPIO.cleanup()
