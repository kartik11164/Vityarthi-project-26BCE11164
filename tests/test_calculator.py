"""Basic validation tests for grade calculation functions."""

import unittest

from app.calculator import calculate_average, calculate_grade, calculate_result, calculate_total


class TestCalculator(unittest.TestCase):
    """Test totals, averages, grades, and final results."""

    def setUp(self):
        self.passing_marks = [
            {"subject": "Python", "mark": 90},
            {"subject": "Maths", "mark": 80},
            {"subject": "English", "mark": 70},
            {"subject": "Physics", "mark": 60},
            {"subject": "Chemistry", "mark": 50}
        ]

    def test_total(self):
        self.assertEqual(calculate_total(self.passing_marks), 350)

    def test_average(self):
        self.assertEqual(calculate_average(self.passing_marks), 70)

    def test_grade_boundaries(self):
        self.assertEqual(calculate_grade(90), "A+")
        self.assertEqual(calculate_grade(80), "A")
        self.assertEqual(calculate_grade(40), "D")
        self.assertEqual(calculate_grade(39), "F")

    def test_result_fails_if_one_mark_is_below_40(self):
        failed_marks = self.passing_marks.copy()
        failed_marks[2] = {"subject": "English", "mark": 30}
        self.assertEqual(calculate_result(failed_marks), "Fail")


if __name__ == "__main__":
    unittest.main()

