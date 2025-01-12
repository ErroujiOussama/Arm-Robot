import roboticstoolbox as rtb
import swift
import numpy as np
import spatialmath as sm
import spatialgeometry as sg
import serial  # For Arduino communication

# Initialize serial communication with Arduino
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Replace with your Arduino's port

# Load the URDF model
env = swift.Swift()
env.launch(realtime=True)
robot = rtb.Robot.URDF("/Users/OUSSAMA/Desktop/projects/WIP/Arm robot project/5- simulation/robotics_tool_box_python/arm_robot/robot.urdf")

# Set joint limits (in radians, matching Arduino limits)
robot.qlim = np.radians([[0, 180], [0, 90], [0, 180], [0, 180], [0, 90], [0, 50]])

# Add the robot to the environment
env.add(robot)

# Joint offsets (to account for mismatches in simulation vs. real robot)
JOINT_OFFSETS = [0, 0, 0, 0, 0, 0]  # Adjust offsets as needed for each joint
arduino_offsets = [180, 60, 93, 93.6, 10.8, 0]  # Replace with your exact values if necessary

# Convert offsets to radians (roboticstoolbox uses radians)
arduino_offsets_rad = np.radians(arduino_offsets)

# Set the robot's initial joint configuration to match Arduino values
robot.q = arduino_offsets_rad
# Function to send joint angles to Arduino
def send_to_arduino(joint_angles):
    # Normalize and apply offsets
    joint_angles = np.clip(np.degrees(joint_angles), [0, 0, 0, 0, 0, 0], [180, 90, 180, 180, 90, 50])
    joint_angles = [angle + JOINT_OFFSETS[i] for i, angle in enumerate(joint_angles)]
    data = ",".join([f"{int(angle)}" for angle in joint_angles]) + "\n"
    ser.write(data.encode())
    print(f"Sent to Arduino: {data.strip()}")

# Test individual joint movement
def test_joint(joint_index, duration=2):
    """
    Test a single joint by moving it from 0 to 180 degrees and back to 0.
    :param joint_index: Index of the joint to test (0 to 5)
    :param duration: Duration for each step (in seconds)
    """
    # Move joint to 0 degrees
    robot.q[joint_index] = np.radians(0)
    send_to_arduino(robot.q)
    env.step()
    print(f"Joint {joint_index} at 0 degrees")
    env.sleep(duration)

    # Move joint to 180 degrees
    robot.q[joint_index] = np.radians(180)
    send_to_arduino(robot.q)
    env.step()
    print(f"Joint {joint_index} at 180 degrees")
    env.sleep(duration)

    # Move joint back to 0 degrees
    robot.q[joint_index] = np.radians(0)
    send_to_arduino(robot.q)
    env.step()
    print(f"Joint {joint_index} back to 0 degrees")
    env.sleep(duration)

# Test the function with a specific joint
test_joint(0)  # Test the base joint (adjust index for other joints)
