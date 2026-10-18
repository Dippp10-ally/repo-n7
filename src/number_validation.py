"""Numeric validation helpers."""


def is_positive_int(value):
    """Return True when value is a positive integer."""
    return isinstance(value, int) and value > 0
