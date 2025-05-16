#Program for a LEGO EV3 robot that autonomously collects and transports a red LEGO block and a yellow LEGO block to designated positions while avoiding all other blocks.
#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor, abc)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
# Initialize the EV3 Brick
ev3 = EV3Brick()

# Initialize motors for movement and gripping
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
grip_motor = Motor(Port.A)

# Initialize the sensors
obstacle_sensor = UltrasonicSensor(Port.S3)  # Ultrasonic Sensor on Port 4
color_sensor = ColorSensor(Port.S4)    # Color Sensor on Port 1

# Settings
turn_rate = 0
speed = 100
# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
robot.drive(speed, turn_rate)
# Drop off locations
RED_DROP_OFF = (50, 50)
YELLOW_DROP_OFF = (100, 100)

# Get the sensor values
distance = obstacle_sensor.distance()  # Distance in millimeters
color = color_sensor.color()      # Detected color (numeric code)

# Play a custom beep sequence when the task is completed
def play_custom_beep_sequence():
    ev3.speaker.beep(440, 500)  # Beep at 440 Hz for 500 ms
    wait(100)              # Wait 100 ms between beeps
    ev3.speaker.beep(660, 500)  # Beep at 660 Hz for 500 ms
    wait(100)
    ev3.speaker.beep(880, 500)  # Beep at 880 Hz for 500 ms

# Function to move the robot forward
def move_forward(speed, duration):
    left_motor.run(speed)
    right_motor.run(speed)
    wait(duration)
    left_motor.stop()
    right_motor.stop()

# Function to turn the robot
def turn(angle):
    left_motor.run_angle(100, angle, then=Stop.HOLD, wait=True)
    right_motor.run_angle(100, -angle, then=Stop.HOLD, wait=True)

# Function to grip a block
def grip_block():
    grip_motor.run_until_stalled(500, then=Stop.HOLD)

# Function to release a block
def release_block():
    grip_motor.run_until_stalled(-500, then=Stop.HOLD)

# Function to navigate to a specific drop-off position
def navigate_to_position(target_x, target_y):
    # Example logic assuming basic movement corrections
    while True:
        distance = obstacle_sensor.distance()
        
        if distance < 100:  # Avoid obstacles
            turn(90)  # Turn away from obstacles
        else:
            move_forward(200, 500)  # Move towards the target

        # Stop if close to the destination (simplified logic)
        if abs(target_x - robot.state[0]) < 10 and abs(target_y - robot.state[1]) < 10:
            break

# Main logic
while True:
    # Get the sensor values
    distance = obstacle_sensor.distance()  # Distance in millimeters
    color = color_sensor.color()      # Detected color (numeric code)
    # Display the values on the EV3 Brick screen
    ev3.screen.clear()
    ev3.screen.draw_text(10, 10, "Distance: {} mm".format(distance))
    ev3.screen.draw_text(10, 30, "Color: {}".format(color))
    # Wait before updating the values (500ms)
    wait(500)

    # Move forward and scan for blocks
    move_forward(200, 1000)  # Adjust speed and duration
    detected_color = color_sensor.color()

    if detected_color == Color.RED:
        play_custom_beep_sequence()  # Beep sequence when red block detected
        grip_block()
        # Navigate to red block drop-off position
        navigate_to_position(*RED_DROP_OFF)  # Move to red drop-off
        release_block()

    elif detected_color == Color.YELLOW:
        play_custom_beep_sequence()  # Beep sequence when yellow block detected
        grip_block()
        # Navigate to yellow block drop-off position
        navigate_to_position(*YELLOW_DROP_OFF) #move to yellow drop off
        release_block()

    elif detected_color != Color.NONE:  # Avoid other blocks
        turn(90)  # Example: Turn 90 degrees to avoid

    # Stop condition (add specific logic, e.g., a timer or manual stop)
    # Example: break if task is completed
        
# Explanation:
#1.Initialization: The robot is set up with motors and a color sensor. Gripping and releasing actions are handled by the grip_motor.
#2.Block Detection: The robot moves forward, continuously checking for red or yellow blocks. If detected, it collects the block using the gripping motor.
#3.Navigation to Drop-off Zones: You need to define the navigation logic to steer the robot toward the target position for each block.
#4.Avoiding Other Blocks: Non-red and non-yellow blocks are avoided by executing a turn.
#5.Repetition: The robot repeats these steps until all blocks are transported to their respective drop-off zones.