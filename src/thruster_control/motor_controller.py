"""Basic differential-thrust control for the two USV thrusters."""

import time

try:
    from gpiozero import Servo
except ImportError:
    Servo = None


LEFT_GPIO = 17
RIGHT_GPIO = 18


class ThrusterController:
    """Controls left and right ESC signals through Raspberry Pi GPIO."""

    def __init__(self, left_gpio: int = LEFT_GPIO, right_gpio: int = RIGHT_GPIO):
        if Servo is None:
            raise RuntimeError("gpiozero is required when running on the Raspberry Pi")
        self.left = Servo(left_gpio, min_pulse_width=0.001, max_pulse_width=0.002)
        self.right = Servo(right_gpio, min_pulse_width=0.001, max_pulse_width=0.002)

    def set_thrust(self, left: float, right: float) -> None:
        self.left.value = max(-1.0, min(1.0, left))
        self.right.value = max(-1.0, min(1.0, right))

    def forward(self, speed: float = 0.25) -> None:
        self.set_thrust(speed, speed)

    def turn_left(self, speed: float = 0.25) -> None:
        self.set_thrust(-speed, speed)

    def turn_right(self, speed: float = 0.25) -> None:
        self.set_thrust(speed, -speed)

    def stop(self) -> None:
        self.set_thrust(0.0, 0.0)


if __name__ == "__main__":
    controller = ThrusterController()
    try:
        controller.forward(0.20)
        time.sleep(2)
    finally:
        controller.stop()
