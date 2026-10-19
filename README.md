# Triangle Classifier

## Why an Equilateral Triangle Can Never Be a Right Triangle

An equilateral triangle can never also be right as it has all equal sides, meaning all angles are 60°. A right triangle requires one angle to be 90°, rendering it impossible for an equilateral triangle to have any right angles.

# Triangle Testing & Copilot Review Log

## How to Run the Tests

To run the tests, ensure you have `pytest` installed. Then, enter and execute the following command in the terminal:
pytest test_triangle.py

## Equivalence Classes

Valid Triangles: Equilateral (all sides equal), Isosceles (Exactly two sides equal), Scalene (All sides different), and Right Triangles (Satisfies Pythagorean theorem). 
Invalid Triangles: Any side <= 0, triangles which fail triangle inequality (e.g., sum of two sides <= third side)

## Boundary Cases

Degenerate Triangle: The sum of two sides equals third side (e.g., 1, 2, 3).
Non-Integer Case: Right triangles with non-integer sides (e.g., 5, 5, 5√2).

## Copilot Review Log

| Test Name | Copilot-suggested? | Kept / Edited / Rejected | Why? |
| :--- | :--- | :--- | :--- |
| `test_invalid_triangle` | Yes | Kept | Correctly passed three tests for invalid cases, including zero side, negative side, and triangle inequality fails. |
| `test_equilateral_triangle` | Yes | Kept | Copilot's suggestion matched the spec for equilateral triangles.. |
| `test_isosceles_triangle` | Yes | Kept | Correctly passed two equal sides that satisfy the triangle inequality. |
| `test_scalene_triangle` | Yes | **Rejected** | **Caught Mistake:** Copilot hallucinated that `(1, 2, 3)` was a valid `Scalene` triangle. Removed and added as degenerate case in `test_invalid_triangle`. |
| `test_right_triangle` | Yes | Kept | Correctly passed two equal sides that satisfy the triangle inequality. |
| `test_right_triangle_non_integer` | Yes | **Edited** | **Caught Mistake:** Included pytest.approx(), which is a special wrapper. Edited to remove `pytest.approx()` to pass raw floats. |

## Acceptance Criteria

**Given** a customer enters three side lengths.
**When** the sides lengths indicate an invalid triangle.
**Then** the system should display a message indicating that the triangle is invalid and not attempt to build it.
**Given** a customer enters angled pieces.
**When** one angle indicates a right angled triangle.
**Then** the system should flag the triangle as requiring reinforced corners.
**Given** a customer enters three side lengths.
**When** the side lengths indicate a valid triangle.
**Then** the system should display the shape of the triangle (equilateral, isosceles, or scalene) and confirm that it is buildable.

## AI-use Disclosure

Tool: GitHub Copilot, Use: drafting skeleton for triangle.py and test_triangle.py. Reviewed and verified tests in test_triangle.py. No other AI tool used.
