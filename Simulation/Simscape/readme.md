# Simscape Robot Arm Control Project

![alt text](<img/all frames and transforms.png>) 
![alt text](<img/center of mass.png>)

The model is structured as a **Rigid Body Tree**, which is subsequently transformed into a Simscape model. The Simscape model allows control over the arm's actuation through motion and torque inputs.

![alt text](<img/general block.png>)


### **Actuation Control**:
   - Control the motion and torque of the arm's joints.

![alt text](img/slider.png)

### **Control System Design**:
   - **Low-Level Control**: Adjust motion inputs directly using sliders.
   - **High-Level Control**: Implement a PID controller to manage motion and torque inputs.

#### Low-Level Control (Motion Control)
- Use the slider blocks in Simulink to adjust the motion of individual joints.

#### High-Level Control (PID Control)
- Use the provided PID controller block to control both motion and torque.
- Adjust the PID parameters to optimize performance.

## Future Work
- Extend the control system to support trajectory planning.
- Integrate ROS for real-time control and feedback.


