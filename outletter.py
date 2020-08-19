#for use with websocket webserver
import RPi.GPIO as GPIO
import time,sys

#setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#gpio pins to control stepper motor
GPIO.setup(8, GPIO.OUT, initial=0)


if __name__ == "__main__":
    statearg=int(sys.argv[1])
    print(statearg)
    try:
        if statearg==0:
            GPIO.output(8,1)
            time.sleep(0.5)
            print("off")
        elif statearg==1:
            GPIO.output(8,0)
            time.sleep(0.5)
            print("on")
        else:
            print("Bad input")
        
    except KeyboardInterrupt:
        GPIO.cleanup()   

