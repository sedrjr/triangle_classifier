import math
import pytest
from triangle import is_valid_triangle, classify_triangle

def test_invalid_triangle():
    # Any side ≤ 0 or triangle inequality fails
    assert classify_triangle(0, 4, 5) == "Invalid"  # Zero side
    assert classify_triangle(-1, 4, 5) == "Invalid"  # Negative side
    assert classify_triangle(1, 1, 3) == "Invalid"  # Triangle inequality fails
    assert classify_triangle(1, 2, 3) == "Invalid"  # Degenerate case

def test_equilateral_triangle():
    # All sides equal
    assert classify_triangle(3, 3, 3) == "Equilateral"

def test_isosceles_triangle():
    # Exactly two sides equal
    assert classify_triangle(3, 3, 5) == "Isosceles"
    assert classify_triangle(5, 3, 3) == "Isosceles"
    assert classify_triangle(3, 5, 3) == "Isosceles"

def test_scalene_triangle():
    # All sides different
    assert classify_triangle(7, 8, 9) == "Scalene"

def test_right_triangle():
    # Satisfies the Pythagorean theorem
    assert classify_triangle(3, 4, 5) == "Right Scalene"
    assert classify_triangle(5, 12, 13) == "Right Scalene"

def test_right_triangle_non_integer():
    # Right triangle with non-integer sides
    assert classify_triangle(5, 5, 5 * math.sqrt(2)) == "Right Isosceles"