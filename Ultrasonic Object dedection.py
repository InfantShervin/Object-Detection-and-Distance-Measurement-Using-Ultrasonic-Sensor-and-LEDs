import RPi.GPIO as GPIO
import time

# GPIO pin setup
# gpio pin ste up as coded below 
#follow step by step instruction 
GPIO.setmode(GPIO.BCM)
TRIG = 18    # Ultrasonic Trigger pin
ECHO = 24    # Ultrasonic Echo pin
GREEN_LED = 17  # Green LED pin
YELLOW_LED = 27 # Yellow LED pin
RED_LED = 22    # Red LED pin
BUZZER = 23     # Buzzer pin

# Set up pins as output or input
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(YELLOW_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(BUZZER, GPIO.OUT)

def measure_distance():
    # Trigger a pulse
    GPIO.output(TRIG, True)
    time.sleep(0.00001) # 10 microseconds
    GPIO.output(TRIG, False)

    # Measure echo pulse duration
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    # Calculate distance based on pulse duration
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # speed of sound = 34300 cm/s
    return round(distance, 2)

def control_lights_and_buzzer(distance):
    # Define thresholds
    safe_distance = 50   # Safe range in cm
    caution_distance = 30 # Caution range in cm
    close_distance = 10  # Close range in cm

    # Reset all indicators
    GPIO.output(GREEN_LED, False)
    GPIO.output(YELLOW_LED, False)
    GPIO.output(RED_LED, False)
    GPIO.output(BUZZER, False)

    # Determine which indicators to turn on based on distance
    if distance > safe_distance:
        GPIO.output(GREEN_LED, True)
    elif caution_distance < distance <= safe_distance:
        GPIO.output(YELLOW_LED, True)
    elif close_distance < distance <= caution_distance:
        GPIO.output(RED_LED, True)
    elif distance <= close_distance:
        GPIO.output(RED_LED, True)
        GPIO.output(BUZZER, True)

try:
    while True:
        distance = measure_distance()
        print("Measured Distance:", distance, "cm")
        control_lights_and_buzzer(distance)
        time.sleep(1) # Update every second

except KeyboardInterrupt:
    print("Program stopped by user.")
    GPIO.cleanup()
