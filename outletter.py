#for use with websocket webserver
import RPi.GPIO as GPIO
import time,sys

#setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#gpio pins to control stepper motor
GPIO.setup(8, GPIO.OUT)


if __name__ == "__main__":
    try:
        if sys.argv[1]=="1":
            GPIO.output(8,1)
        elif sys.argv[1]=="0":
            GPIO.output(8,0)
        else:
            print("Bad input")
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()   

