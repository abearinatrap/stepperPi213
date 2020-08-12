#for use with websocket webserver
import RPi.GPIO as GPIO
import time,sys

#setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#gpio pins to control stepper motor
pinOut=[7,11,13,15]
for SPin in pinOut:
    GPIO.setup(SPin, GPIO.OUT)

def setStep(pin1,pin2,pin3,pin4):
    GPIO.output(pinOut[0],pin1)
    GPIO.output(pinOut[1],pin2)
    GPIO.output(pinOut[2],pin3)
    GPIO.output(pinOut[3],pin4)

Seq=[[1,0,0,1],[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1]]

def clockWc(delay):
    while True:
        for j in Seq:
            setStep(j[0],j[1],j[2],j[3])
            time.sleep(delay)
    setStep(0,0,0,0)
def clockBc(delay):
    while True:
        for j in Seq:
            setStep(j[3],j[2],j[1],j[0])
            time.sleep(delay)
    setStep(0,0,0,0)
if __name__ == "__main__":
    delay=int(sys.argv[1])
    if delay<0:
        clockBc(-(50/delay)/1000.0)
    elif delay>0:
        clockWc((50/delay)/1000.0)
    else:
	#nothing
	print("nothing")
