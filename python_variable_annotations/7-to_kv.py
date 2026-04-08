#!/usr/bin/env python3
"""Module for creating a key-value tuple from a string and a number."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple of the string k and the square of v as a float."""
    return (k, v ** 2)
