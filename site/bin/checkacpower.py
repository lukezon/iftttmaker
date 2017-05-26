import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
pin = 7
GPIO.setup(pin, GPIO.IN)

def getpowerstatus(initpolls = 10000, checks = 100):
	power = 0
	for l in range(checks):
		polls = initpolls
		for l in range(initpolls):
			if GPIO.input(pin) == GPIO.LOW:
				polls = polls - 1
		if polls < initpolls:
			power = power + 1
		else:
			power = power - 1
	if power < 0:
		return 0
	elif power > 0:
		return 1
	else:
		return "Error Reading Sonic Sensor"



if __name__ == "__main__":
	print getpowerstatus()

