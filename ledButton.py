import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

blinkCount = 100
count = 0

LEDPin = 22
buttonPin = 5
# Setup the pin the LED is connected to
GPIO.setup(LEDPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

buttonPress = True
ledState = False

try:
	while count < blinkCount:
		print("Press the button")
		buttonPress = GPIO.input(buttonPin)
		if buttonPress == False and ledState == False:
			GPIO.output(LEDPin, True)
			print("LED ON")
			ledState = True
		elif buttonPress == False and ledState == True:
			GPIO.output(LEDPin, False)
			print("LED OFF")
			ledState = False
			count +=1
		sleep(0.1)
finally:
	GPIO.output(LEDPin, False)
	GPIO.cleanup()
