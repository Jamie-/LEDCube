import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

## When looking from the top, col1 is the top left and col4 is the
## bottom right. They go numerically left to right so col2 is top
## right and col3 is bottom left.

## NOTE: The columns will need transistors to work - the transistor
## works like a switch to ground (or 0V).

## In order to turn one LED on, it's column and it's layer must be 
## enabled. This basically connects the LED to ground (column
## transistor) and +3.3V (direct to the GPIO).s


## Defining the pins ##
def wait = 150
def topLayer = 0 # GPIO pin for top layer
def botLayer = 0 # GPIO pin for bottom layer

def col1 = 0 # GPIO pin for column 1
def col2 = 0 # GPIO pin for column 2
def col3 = 0 # GPIO pin for column 3
def col4 = 0 # GPIO pin for column 4

## Setting the pins ##
GPIO.setup(topLayer, GPIO.OUT)
GPIO.output(topLayer, False)
GPIO.setup(botLayer, GPIO.OUT)
GPIO.output(botLayer, False)
GPIO.setup(col1, GPIO.OUT)
GPIO.output(col1, False)
GPIO.setup(col2, GPIO.OUT)
GPIO.output(col2, False)
GPIO.setup(col3, GPIO.OUT)
GPIO.output(col3, False)
GPIO.setup(col4, GPIO.OUT)
GPIO.output(col4, False)

## Test to start - all LEDs should light up. ##
GPIO.output(topLayer, True)
GPIO.output(botLayer, True)
GPIO.output(col1, True)
GPIO.output(col2, True)
GPIO.output(col3, True)
GPIO.output(col4, True)
time.sleep(1000)
GPIO.output(topLayer, False)
GPIO.output(botLayer, False)
GPIO.output(col1, False)
GPIO.output(col2, False)
GPIO.output(col3, False)
GPIO.output(col4, False)
## ------------------------------ ##

## Loop for the animations! ##
## Every blank line signifies an output change ##
while True :
	# Animation 1 - up, across, down
	GPIO.output(botLayer, True)
	GPIO.output(col1, True)
	GPIO.output(col2, True)
	time.sleep(wait)
	
	GPIO.output(topLayer, True)
	time.sleep(wait)
	
	GPIO.output(col1, False)
	GPIO.output(col2, False)
	GPIO.output(col3, True)
	GPIO.output(col4, True)
	time.sleep(wait)
	
	GPIO.output(topLayer, False)
	time.sleep(wait)
	
	GPIO.output(botLayer, False)
	time.sleep(wait)
	
	# Animation 2 - up, down
	GPIO.output(botLayer, True)
	GPIO.output(col1, True)
	GPIO.output(col2, True)
	GPIO.output(col3, True)
	GPIO.output(col4, True)
	time.sleep(wait)
	
	GPIO.output(topLayer, True)
	time.sleep(wait)
	
	GPIO.output(topLayer, False)
	time.sleep(wait)
	
	GPIO.output(botLayer, False)
	GPIO.output(col1, False)
	GPIO.output(col2, False)
	GPIO.output(col3, False)
	GPIO.output(col4, False)
	time.sleep(wait)
	
	# Animation 3
	GPIO.output(botLayer, True)
	GPIO.output(topLayer, True)
	GPIO.output(col1, True)
	GPIO.output(col2, True)
	time.sleep(wait)
	
	GPIO.output(col1, False)
	GPIO.output(col2, False)
	GPIO.output(col3, True)
	GPIO.output(col4, True)
	time.sleep(wait)
	
	GPIO.output(botLayer, False)
	GPIO.output(topLayer, False)
	GPIO.output(col3, False)
	GPIO.output(col4, False)
	time.sleep(wait)
	
	