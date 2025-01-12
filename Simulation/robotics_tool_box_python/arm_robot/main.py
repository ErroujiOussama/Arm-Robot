import roboticstoolbox as rtb
import swift
import numpy as np 
import spatialmath as sm
import spatialgeometry as sg
# Load the URDF model
env = swift.Swift()
env.launch(realtime=True)
robot = rtb.Robot.URDF("/Users/OUSSAMA/Desktop/projects/WIP/Arm robot project/5- simulation/robotics_tool_box_python/arm_robot/robot.urdf")
tool_transform = sm.SE3.Tx(0) * sm.SE3.Ty(0) * sm.SE3.Tz(0) * sm.SE3.RPY(0, 0, -45, unit='deg')
#Assign the tool transform to the robot
robot.tool = tool_transform

env.add(robot)

def move_to_position(x, y, z):
    # Define the target end-effector pose as an absolute position
    Tep = sm.SE3(x, y, z)*sm.SE3.RPY(0, 180, 0, unit='deg')
    # Visualize the target position
    axes = sg.Axes(length=0.1,pose=Tep)
    env.add(axes)
    dt = 0.01
    arrived = False
    iter = 0
    while not arrived and iter < 100:
        iter+=1
        # Compute the control command using position-based servoing
        v, arrived = rtb.p_servo(robot.fkine(robot.q), Tep, gain=2, threshold=0.01)
        # Compute the robot's Jacobian
        J = robot.jacobe(robot.q)
        # Compute the joint velocities using the pseudoinverse of the Jacobian
        robot.qd = np.linalg.pinv(J) @ v
        # Step the simulation
        env.step(dt)
    print(f"Arrived at x={x}, y={y}, z={z}")


for i in range(1, 10):    
    move_to_position(0.01*i+0.2,0,0.1)

for i in range(1, 10):    
    move_to_position(0,0.01*i+0.2,0.1)

for i in range(1, 10):    
    move_to_position(0,0,0.01*i+0.2)

