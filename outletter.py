#for use with websocket webserver
import RPi.GPIO as GPIO
import time,sys

#setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#gpio pins to control stepper motor
GPIO.setup(8, GPIO.OUT)


if __name__ == "__main__":
    statearg=int(sys.argv[1])
    print(statearg)
    try:
        if statearg==1:
            GPIO.output(8,1)
            time.sleep(0.5)
            print("on")
        elif statearg==0:
            GPIO.output(8,0)
            time.sleep(0.5)
            print("off")
        else:
            print("Bad input")
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()   

