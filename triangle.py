import math

def is_valid_triangle(a, b, c) -> bool:
    """
    Check if the given sides form a valid triangle.

    Args:
        a (float): Length of side a.
        b (float): Length of side b.
        c (float): Length of side c.

    Returns:
        bool: True if the sides form a valid triangle, False otherwise.
    """
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b > c and a + c > b and b + c > a

def classify_triangle(a, b, c) -> str:
    """
    Classify a triangle based on the lengths of its sides.

    Args:
        a (float): Length of side a.
        b (float): Length of side b.
        c (float): Length of side c.

    Returns:
        str: Type of triangle.
    """
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    # Check for right triangle using Pythagorean theorem with a tolerance
    sides = sorted([a, b, c])
    if math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2, rel_tol=1e-9):
        right_prefix = "Right "
    else:
        right_prefix = ""

    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return f"{right_prefix}Isosceles"
    else:
        return f"{right_prefix}Scalene"