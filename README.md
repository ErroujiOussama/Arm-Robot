# Arm-Robot

## 3D Model

## Kinematics

## Hardaware

## Simulation 

### 1. PyBullet Robot Simulation

#### Overview
This Project provides a simulation setup using PyBullet to load and control a robot model.

![alt text](<Simulation/pybullet/img/gui 1.jpg>)

#### Features
- **Gravity and Physics Setup**: Configures gravity in the simulation.
- **Joint Control**: Creates sliders for each robot joint to control their positions interactively.

![alt text](<img/gui 2.jpg>)

- **Collision Detection**: Detects and logs collisions between the robot's links and other objects in the environment.

![alt text](<Simulation/pybullet/img/collision detection .jpg>)

#### Notes
- The simulation runs at 240 Hz by default.


### 2. Roboticstoolbox (python)

This code combines simulation, kinematics, and control to visualize the motion of a robot arm.
![alt text](simulation/robotics_tool_box_python/arm_robot/img/swift_snap0.png)
#### **Libraries and Tools**
- roboticstoolbox: Used for modeling and controlling robots.
- swift: Provides a 3D visualization interface for robotics simulation.
- spatialmath: Handles transformations like rotations and translations.
- spatialgeometry: Adds geometric primitives for visualization.

#### **Functions**
- move_to_position:
Moves the robot's end-effector to a target position using servoing.
Computes joint velocities using the Jacobian and pseudoinverse.

#### **Execution**
Sequential movements along the x, y, and z axes demonstrate the robot’s capability.

![alt text](<simulation/robotics_tool_box_python/arm_robot/img/swift_snap (1).png>) 

![alt text](<simulation/robotics_tool_box_python/arm_robot/img/swift_snap (2).png>) 

![alt text](simulation/robotics_tool_box_python/arm_robot/img/swift_snap.png)

#### **Details**:
##### **Servoing**:
Servoing is a feedback-based control technique that continuously adjusts the robot's motion to minimize the error between the current position (or pose) and the desired target position (or pose).
The function rtb.p_servo is used for position-based servoing.
- It calculates a velocity command v for the end-effector, based on the error between:
    
    - The current pose of the end-effector (from robot.fkine(robot.q)).
    
    - The target pose (Tep).
    
 - The gain parameter scales how aggressively the robot corrects the error.
 - The threshold parameter (set to 0.01) defines how close the end-effector must get to the target pose to consider the movement complete.

=> Servoing ensures that the end-effector dynamically adjusts its motion to precisely reach the target position.

##### **Jacobian Matrix (J)**
Maps joint velocities (`qd`) to end-effector velocity (`v`):
```
v = J * qd
```
##### **Pseudoinverse of Jacobian**
For non-square `J`, use the pseudoinverse (`J⁺`) to calculate `qd`:
```
qd = J⁺ * v
```
##### **In Code**
- `robot.jacobe(robot.q)`: Compute `J`.
- `np.linalg.pinv(J)`: Compute `J⁺`.
- `robot.qd = np.linalg.pinv(J) @ v`: Calculate `qd` for the desired `v`.


#### Dependencies
Ensure the following libraries are installed in your Python environment:
```
roboticstoolbox
swift
numpy 
spatialmath
spatialgeometry
```
#### Note
1- Update the paths in the URDF file to match your local system. For example:
```
<mesh filename="/Users/OUSSAMA/Desktop/projects/WIP/Arm robot project/5- simulation/robotics_tool_box_python/arm_robot/arm_01.stl"/>
```
2- Update the path in python coode:
```
robot = rtb.Robot.URDF("/Users/OUSSAMA/Desktop/projects/WIP/Arm robot project/5- simulation/robotics_tool_box_python/arm_robot/robot.urdf")
```

### 3. Simscape Robot Arm Control

![alt text](<img/all frames and transforms.png>) 
![alt text](<img/center of mass.png>)

The model is structured as a **Rigid Body Tree**, which is subsequently transformed into a Simscape model. The Simscape model allows control over the arm's actuation through motion and torque inputs.

![alt text](<img/general block.png>)


#### **Actuation Control**:
   - Control the motion and torque of the arm's joints.

![alt text](img/slider.png)

##### **Control System Design**:
   - **Low-Level Control**: Adjust motion inputs directly using sliders.
   - **High-Level Control**: Implement a PID controller to manage motion and torque inputs.

##### Low-Level Control (Motion Control)
- Use the slider blocks in Simulink to adjust the motion of individual joints.

##### High-Level Control (PID Control)
- Use the provided PID controller block to control both motion and torque.
- Adjust the PID parameters to optimize performance.

## Arduino Programming

## AI Model
