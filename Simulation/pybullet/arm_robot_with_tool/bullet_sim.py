import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI) 

# Set the path for URDFs
p.setAdditionalSearchPath(pybullet_data.getDataPath())  

# Set Gravity
p.setGravity(0, 0, -9.81)

# Load Plane and Robot URDF
p.loadURDF("plane.urdf")  # Load a plane as the ground
robot_id = p.loadURDF("robot.urdf", useFixedBase=True)

# Get the number of joints in the robot
num_joints = p.getNumJoints(robot_id)

# Create sliders for each joint
joint_sliders = []
for joint in range(num_joints):
    joint_info = p.getJointInfo(robot_id, joint)
    joint_name = joint_info[1].decode("utf-8")
    joint_sliders.append(
        p.addUserDebugParameter(joint_name, -3.14, 3.14, 0)  # Range [-π, π]
    )

# Run the simulation:
while True:
    p.stepSimulation()
    # Update joint positions based on sliders
    for joint, slider in enumerate(joint_sliders):
        joint_value = p.readUserDebugParameter(slider)
        p.setJointMotorControl2(
            bodyUniqueId=robot_id,
            jointIndex=joint,
            controlMode=p.POSITION_CONTROL,
            targetPosition=joint_value
        )
    
    # Visualize collisions
    collisions = p.getContactPoints(bodyA=robot_id)
    if collisions:
        print("Collision detected at links:", [c[3] for c in collisions])

    time.sleep(1 / 240)
