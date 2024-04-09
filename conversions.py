def point2inch(value: float) -> float:
    """Converts points to inches."""
    return value / 72.0


def inch2point(value: float) -> float:
    """Converts inches to points."""
    return value * 72.0


def mm2inch(value: float) -> float:
    """Converts millimeters to inches."""
    return value / 25.4


def inch2mm(value: float) -> float:
    """Converts inches to millimeters."""
    return value * 25.4


def mm2point(value: float) -> float:
    """Converts millimeters to points."""
    return inch2point(mm2inch(value))


def point2mm(value: float) -> float:
    """Converts points to millimeters."""
    return inch2mm(point2inch(value))
