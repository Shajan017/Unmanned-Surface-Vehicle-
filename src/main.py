"""Main integration entry point for the USV software.

The project is intentionally split into modules. Hardware-specific
initialisation can be enabled after each component has been tested safely.
"""

from ai_detection.waste_detection import MODEL_PATH
from navigation.navigation_controller import NavigationController
from sensors.imu import normalize_heading
from sensors.wind_sensor import relative_wind_angle


def main() -> None:
    print("USV software starting...")
    print(f"AI model path: {MODEL_PATH}")

    navigation = NavigationController()
    current_heading = normalize_heading(10.0)
    target_heading = 25.0
    left, right = navigation.calculate_thrust(target_heading, current_heading)

    print(f"Navigation command -> left={left:.2f}, right={right:.2f}")
    print(
        "Relative wind angle:",
        relative_wind_angle(current_heading, wind_direction=45.0),
    )
    print("Hardware integration can be enabled after bench testing.")


if __name__ == "__main__":
    main()
