# Navigation

The navigation system is designed around differential thrust.

## Inputs

- GPS position
- IMU/compass heading
- Target direction
- Wind direction

## Control loop

```text
Read sensors
    ↓
Estimate current state
    ↓
Calculate target heading
    ↓
Find heading error
    ↓
Apply correction
    ↓
Set left/right thruster commands
    ↓
Repeat
```

## Wind compensation

Wind direction can be used as an additional correction term. The first version should be tested in calm water, followed by controlled disturbance tests.

## Testing

Navigation performance should eventually be reported using actual waypoint error, heading error and drift measurements. Values should not be added until they are measured during testing.
