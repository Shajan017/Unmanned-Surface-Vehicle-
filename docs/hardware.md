# Hardware Documentation

## Main controller

**Raspberry Pi 4 (8 GB)** is planned as the main onboard computer. It handles AI inference, sensor processing and high-level control.

## Propulsion

The prototype uses a differential-thrust concept with a left and right brushless underwater thruster. ESCs are used to control the motors.

## Sensors

- Camera – visual detection
- GPS – position
- IMU/compass – orientation
- Wind sensor – wind direction

## Power

A 3S 11.1 V LiPo battery has been considered for the prototype. The final battery and regulator arrangement must be selected according to the actual motor current, Raspberry Pi requirements and safety constraints.

## Mechanical platform

The current concept is a twin-hull platform connected by a rigid frame. The central space is used for electronics and the collection mechanism.

## Important note

Hardware specifications may change during prototype testing. The repository should always be updated with the actual components installed on the latest vehicle version.
