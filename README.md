# Triangle Classifier

## Why an Equilateral Triangle Can Never Be a Right Triangle

An equilateral triangle can never also be right as it has all equal sides, meaning all angles are 60°. A right triangle requires one angle to be 90°, rendering it impossible for an equilateral triangle to have any right angles.

# Triangle Testing & Copilot Review Log

## Copilot Review Log

| Test Name | Copilot-suggested? | Kept / Edited / Rejected | Why? |
| :--- | :--- | :--- | :--- |
| `test_invalid_triangle` | Yes | Kept | Correctly passed three tests for invalid cases, including zero side, negative side, and triangle inequality fails. |
| `test_equilateral_triangle` | Yes | Kept | Copilot's suggestion matched the spec for equilateral triangles.. |
| `test_isosceles_triangle` | Yes | Kept | Correctly passed two equal sides that satisfy the triangle inequality. |
| `test_scalene_triangle` | Yes | **Rejected** | **Caught Mistake:** Copilot hallucinated that `(1, 2, 3)` was a valid `Scalene` triangle. Removed and added as degenerate case in `test_invalid_triangle`. |
| `test_right_triangle` | Yes | Kept | Correctly passed two equal sides that satisfy the triangle inequality. |
| `test_right_triangle_non_integer` | Yes | **Edited** | **Caught Mistake:** Included pytest.approx(), which is a special wrapper. Edited to remove `pytest.approx()` to pass raw floats. |
