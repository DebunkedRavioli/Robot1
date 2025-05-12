#Assesment Task 1 

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from time import sleep

# Initialize EV3 components
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
gripper_motor = Motor(Port.A)  # Main gripper motor
extra_motor = Motor(Port.D)  # Additional motor for block handling
color_sensor = ColorSensor(Port.S1)
ultrasonic_sensor = UltrasonicSensor(Port.S2)

# Define drive base
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=120)

# Function to find and collect a block
def find_block():
    while True:
        if color_sensor.color in [Color.RED, Color.YELLOW]:
            robot.stop()
            return color_sensor.color
        robot.drive(100, 0)  # Move forward

# Function to grip block
def grip_block():
    gripper_motor.run_angle(200, 45)  # Close gripper
    sleep(1)

# Function to release block
def release_block():
    gripper_motor.run_angle(200, -45)  # Open gripper
    sleep(1)

# Function for extra handling (lifting, positioning, securing blocks)
def extra_handling():
    extra_motor.run_angle(150, 30)  # Move end effector for better handling
    sleep(1)

# Function to avoid obstacles
def avoid_obstacles():
    while ultrasonic_sensor.distance() < 100:  # If obstacle detected
        robot.drive(-100, 0)  # Move backward
        sleep(1)
        robot.drive(100, 45)  # Turn away
        sleep(1)

# Main loop to collect and transport blocks
for _ in range(2):  # Collect two blocks
    robot.drive(100, 0)  # Move forward
    block_color = find_block()
    if block_color:
        extra_handling()  # Engage handling mechanism
        grip_block()
        robot.drive_time(500, 0, 3000)  # Move to drop-off location
        release_block()
    avoid_obstacles()

# Return to start position
robot.drive_time(-500, 0, 3000)

