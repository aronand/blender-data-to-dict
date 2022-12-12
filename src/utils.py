from typing import Any


def validate_string(string: str) -> str:
    """Validates the type and value of a given string.

    Returns the given string if valid.
    :raises TypeError: argument type is not str
    :raises ValueError: argument is an empty string
    """
    if type(string) is not str:
        raise TypeError("Argument must be of type str")
    if string == "":
        raise ValueError("Argument can't be an empty string")
    return string


def get_class_name(obj: Any) -> str:
    return type(obj).__name__
