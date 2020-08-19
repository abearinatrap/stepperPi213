#for use with websocket webserver
import RPi.GPIO as GPIO
import time,sys

#setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#gpio pins to control stepper motor
GPIO.setup(8, GPIO.OUT)


# if __name__ == "__main__":
#     if sys.argv[1]=="1":
#         GPIO.output(8,1)
#     elif sys.argv[1]=="0":
#         GPIO.output(8,0)
#     else:
#         print("Bad input")
#     GPIO.cleanup()

try:  
    while True:  
        GPIO.output(8, 1)         # set GPIO24 to 1/GPIO.HIGH/True  
        time.sleep(0.5)                 # wait half a second  
        GPIO.output(8, 0)         # set GPIO24 to 0/GPIO.LOW/False  
        time.sleep(0.5)                 # wait half a second  
  
except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
    GPIO.cleanup()   