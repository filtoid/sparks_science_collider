import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER = 23
GPIO_ECHO = 24
GPIO_TRIGGER_2 = 27
GPIO_ECHO_2 = 22

def get_distance():

	GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
	GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

	# Set trigger to False (Low)
	GPIO.output(GPIO_TRIGGER, False)

	# Allow module to settle
	time.sleep(0.2)

	# Send 10us pulse to trigger
	GPIO.output(GPIO_TRIGGER, True)

	time.sleep(0.00001)

	GPIO.output(GPIO_TRIGGER, False)

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
	
	# Reset GPIO settings
	GPIO.cleanup()
	return distance


def get_distance_2():

        GPIO.setup(GPIO_TRIGGER_2,GPIO.OUT)  # Trigger
        GPIO.setup(GPIO_ECHO_2,GPIO.IN)      # Echo

        # Set trigger to False (Low)
        GPIO.output(GPIO_TRIGGER_2, False)

        # Allow module to settle
        time.sleep(0.2)
        
        # Send 10us pulse to trigger
        GPIO.output(GPIO_TRIGGER_2, True)

        time.sleep(0.00001)
        
        GPIO.output(GPIO_TRIGGER_2, False)

        start = time.time()
        while GPIO.input(GPIO_ECHO_2)==0:
                start = time.time()


        while GPIO.input(GPIO_ECHO_2)==1:
                stop = time.time()

        # Calculate pulse length
        elapsed = stop-start

        # Distance pulse travelled in that time is time
        # multiplied by the speed of sound (cm/s)
        distance = elapsed * 34000

        # That was the distance there and back so halve the value
        distance = distance / 2

        # Reset GPIO settings
        GPIO.cleanup()
        return distance


if __name__ == '__main__':
	get_distance()
	get_distance_2()
