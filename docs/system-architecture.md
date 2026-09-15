# System Architecture

The USV is divided into sensing, AI perception, navigation, propulsion, waste handling and power sections.

## Main flow

```text
Camera → YOLOv8 → Target information → Navigation → ESCs → Thrusters
                     ↑                  ↑
                  GPS / IMU         Wind sensor
```

The Raspberry Pi acts as the main onboard computer. Sensors provide the information required for decision making, while the ESCs provide the interface between the controller and brushless thrusters.

## Design approach

The project is intentionally modular. Each subsystem can be tested independently before full integration. This reduces the chance that a problem in one part of the vehicle will make the entire system difficult to debug.

## Integration order

1. Mechanical platform
2. Power system
3. Thruster control
4. Sensors
5. AI detection
6. Navigation
7. Waste collection
8. Full-system testing
