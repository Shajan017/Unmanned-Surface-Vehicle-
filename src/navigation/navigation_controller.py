"""Simple heading controller for differential-thrust navigation."""

from dataclasses import dataclass


@dataclass
class NavigationController:
    base_speed: float = 0.30
    turn_gain: float = 0.01
    max_speed: float = 0.60

    @staticmethod
    def angle_error(target_heading: float, current_heading: float) -> float:
        """Return the shortest signed heading error in degrees."""
        return (target_heading - current_heading + 180.0) % 360.0 - 180.0

    def calculate_thrust(
        self, target_heading: float, current_heading: float
    ) -> tuple[float, float]:
        error = self.angle_error(target_heading, current_heading)
        correction = self.turn_gain * error

        left = self.base_speed + correction
        right = self.base_speed - correction

        left = max(-self.max_speed, min(self.max_speed, left))
        right = max(-self.max_speed, min(self.max_speed, right))
        return left, right


if __name__ == "__main__":
    controller = NavigationController()
    left, right = controller.calculate_thrust(90.0, 75.0)
    print(f"Left thrust: {left:.2f}, Right thrust: {right:.2f}")
