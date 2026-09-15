"""Small interface for heading data from an IMU/compass."""


def normalize_heading(heading: float) -> float:
    """Convert any compass heading to the 0-360 degree range."""
    return heading % 360.0


if __name__ == "__main__":
    print(normalize_heading(-15.0))
