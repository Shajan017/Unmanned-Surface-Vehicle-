"""Wind-direction helper used by the future drift-compensation module."""


def normalize_wind_direction(direction: float) -> float:
    """Return wind direction as a compass angle from 0 to <360 degrees."""
    return direction % 360.0


def relative_wind_angle(vehicle_heading: float, wind_direction: float) -> float:
    """Calculate the shortest angle between vehicle heading and wind direction."""
    return (wind_direction - vehicle_heading + 180.0) % 360.0 - 180.0
