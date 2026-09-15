"""GPS interface placeholder.

Replace the serial settings and parser with the exact GPS module used in
the prototype. Keeping the sensor interface separate makes the navigation
code easier to test without hardware.
"""

from dataclasses import dataclass


@dataclass
class GPSPosition:
    latitude: float
    longitude: float


def parse_position(latitude: float, longitude: float) -> GPSPosition:
    return GPSPosition(latitude=latitude, longitude=longitude)
