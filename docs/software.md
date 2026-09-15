# Software Documentation

The software is organised into small modules so that individual parts can be tested without running the complete vehicle.

## Planned modules

```text
src/
├── ai_detection/
├── navigation/
├── sensors/
└── thruster_control/
```

## AI detection

The camera frame is passed to the YOLOv8 model. The model returns detected objects, classes and confidence values. Relevant detections are passed to the navigation layer.

## Sensor layer

Sensor drivers provide clean values to the navigation controller. Keeping the hardware interface separate makes it easier to replace a sensor later.

## Navigation layer

The navigation controller uses position and heading information to calculate steering commands.

## Motor layer

The motor-control module converts high-level movement commands into the signal expected by the ESCs.

## Development principle

The software should be tested on a desk or in simulation before enabling the real motors. Motor tests should start at low power and use a safe test procedure.
