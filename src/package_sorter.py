"""
Module for sorting packages according to dimension and mass.
"""

# FIXME: it's not correct to name a function 'sort' as it is a reserved python name
# Anyway, I kept it named like that because the instructions asks clearly to do so
def sort(width_cm: float, height_cm: float, length_cm: float, mass_kg: float) -> str:
    """
    Sort a package into the appropriate stack based on its dimensions and mass.

    Parameters
    ----------
    width_cm : int, float
        Width of the package in centimeters
    height_cm : int, float
        Height of the package in centimeters
    length_cm : int, float
        Length of the package in centimeters
    mass_kg : int, float
        Mass of the package in kilograms

    Returns
    -------
        str: The stack name ("STANDARD", "SPECIAL", or "REJECTED")
    """
    # Input validation
    if not all(
        isinstance(dim, (int, float))
        for dim in [width_cm, height_cm, length_cm, mass_kg]
    ):
        raise ValueError("All dimensions and mass must be numbers")

    if width_cm <= 0 or height_cm <= 0 or length_cm <= 0 or mass_kg <= 0:
        raise ValueError("Dimensions and mass must be greater than zero")

    # Calculate volume
    volume = width_cm * height_cm * length_cm

    # Check if package is bulky
    is_bulky = False
    if volume >= 1e6:
        is_bulky = True
    elif width_cm >= 150 or height_cm >= 150 or length_cm >= 150:
        is_bulky = True

    # Check if package is heavy
    is_heavy = False
    if mass_kg >= 20:
        is_heavy = True

    # Determine the stack
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
