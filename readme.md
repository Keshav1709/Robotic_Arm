# Project Robotic Arm(name-undecided):
Rough initial design sketch.
![Rough](image.png)

# 1. Physical Design

## a. Actuators:
- Nema23: `maximum torque output = 1.89 Nm`
- Nema17: `maximum torque output = 1.0 Nm`

**Things to keep in mind:**<br>
With increase in speed the torque reduces surprisingly quickly. Consider a NEMA 23 stepper motor with a torque rating of 1.9 Nm at low speeds. A typical torque-speed curve might look like this:
  - 0 RPM: 1.9 Nm (maximum torque)<br>
  - 500 RPM: 1.5 Nm
  - 1000 RPM: 1.0 Nm
  - 1500 RPM: 0.5 Nm
  - 2000 RPM: 0.1 Nm
<br>

## b. Gear Reduction:
Render of the Cycloidal drive. A fusion360 plugin was developed to model the cycloid geometrically accurately.

![gearbox](https://cdn.discordapp.com/attachments/1158558503066148894/1241077306072498187/Cycloidal_Gearbox_49_1_v26_Finished_Image.png?ex=6648e2cf&is=6647914f&hm=9ae895c30170aeee0554a7757bb4b8a1e7de90812b760197e426b4f92f5d8138&![image](https://github.com/yup-VARUN/Robotic_Arm/assets/110617721/1c8ae850-d33d-40ce-a9a5-a57829fd6af9)
)

## c. Torque-RPM Characterization Setup:
A load cell based setup would be needed to physically characterizethe performance of the actuator and gearbox combo, that'll be needed in order to tune parameters in the control algorithms.


## d. Base Design:
The arm will be mounted on a platform that could be slided across the x axis with a high precision, to increase the accessible volume by many folds. Sheet metal would be prefered for the base due to cheap price and its manufacturing simplicity(possible to do in-house).
Here's render:

![alt text](image-1.png)

## e. Elbow Joint Design:

## f. First Rotational axis(vertical) design:

## g. Gripper design:


# 2. Electronics Design:

# 3. Software Design:

# Possible Applications:
