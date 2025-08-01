import RPi.GPIO as GPIO
import time

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

motors = {
    "motor1": {"dir": 3, "pul": 4,"ENA":2},
    "motor2": {"dir": 27, "pul": 22, "ENA":17},
    "motor3": {"dir": 9, "pul": 11, "ENA":10},
    "motor4": {"dir": 5, "pul": 6, "ENA":0}
}

def move_motor(motor_name, steps, direction=1, step_delay=0.001):
    """
    Move the specified motor a given number of steps.
    
    :param motor_name: str, key of motor in motors dict
    :param steps: int, number of steps to move
    :param direction: int, 1 or 0, direction of motor
    :param step_delay: float, delay between steps in seconds
    """
    if motor_name not in motors:
        print(f"Motor '{motor_name}' not found.")
        return
    
    motor = motors[motor_name]
    dir_pin = motor["dir"]
    pul_pin = motor["pul"]
    ena_pin = motor["ENA"]
    # Setup pins
    GPIO.setup(dir_pin, GPIO.OUT)
    GPIO.setup(pul_pin, GPIO.OUT)
    GPIO.setup(ena_pin, GPIO.OUT)
    
    GPIO.output(ena_pin, GPIO.LOW)
    # Set direction
    GPIO.output(dir_pin, GPIO.HIGH if direction == 1 else GPIO.LOW)
    
    for _ in range(steps):
        # Pulse high
        GPIO.output(pul_pin, GPIO.HIGH)
        time.sleep(step_delay)
        # Pulse low
        GPIO.output(pul_pin, GPIO.LOW)
        time.sleep(step_delay)
        print("moved")
    print(f"Moved {motor_name} {steps} steps {'forward' if direction == 1 else 'backward'}.")

try:
   
    
    # Example usage: move motor2 100 steps backward
   
    move_motor("motor3", 10000, direction=0, step_delay=0.0005)
finally:
    GPIO.cleanup()
    
