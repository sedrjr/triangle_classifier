import pytest
from triangle import classify_triangle

def test_acceptance_criteria():
    # Test 1: Invalid triangle (triangle inequality fails)
    result = classify_triangle(1, 2, 3)
    assert result == "Invalid", "The system should indicate the triangle is invalid and not buildable."

    # Test 2: Invalid triangle (negative side length)
    result = classify_triangle(-1, 4, 5)
    assert result == "Invalid", "The system should indicate the triangle is invalid and not buildable."

    # Test 3: Right-angled triangle (requires reinforced corners)
    result = classify_triangle(3, 4, 5)
    assert result == "Right Scalene", "The system should flag the triangle as requiring reinforced corners."

    # Test 4: Right-angled isosceles triangle
    result = classify_triangle(5, 5, 5 * 2**0.5)
    assert result == "Right Isosceles", "The system should flag the triangle as requiring reinforced corners."

    # Test 5: Equilateral triangle
    result = classify_triangle(3, 3, 3)
    assert result == "Equilateral", "The system should classify the triangle as equilateral and confirm it is buildable."

    # Test 6: Isosceles triangle
    result = classify_triangle(3, 3, 5)
    assert result == "Isosceles", "The system should classify the triangle as isosceles and confirm it is buildable."

    # Test 7: Scalene triangle
    result = classify_triangle(7, 8, 9)
    assert result == "Scalene", "The system should classify the triangle as scalene and confirm it is buildable."