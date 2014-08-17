import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO_TRIG = 23
GPIO_ECHO = 24

print("Starting measurement")

GPIO.setup(GPIO_TRIG, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

GPIO.output(GPIO_TRIG, False)

time.sleep(0.5)

# Send 10us pulse to trigger
GPIO.output(GPIO_TRIG, True)
time.sleep(0.00001)
GPIO.output(GPIO_TRIG, False)
start = time.time()
while GPIO.input(GPIO_ECHO)==0:
  start = time.time()

while GPIO.input(GPIO_ECHO)==1:
  stop = time.time()

# Calculate pulse length
elapsed = stop-start

# Distance pulse travelled in that time is time
# multiplied by the speed of sound (cm/s)
distance = elapsed * 34000

# That was the distance there and back so halve the value
distance = distance / 2

print("Distance : %.1f" % distance)

# Reset GPIO settings
GPIO.cleanup()


