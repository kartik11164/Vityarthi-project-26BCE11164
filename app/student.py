"""Functions for creating a complete student record."""

from app.calculator import calculate_average, calculate_grade, calculate_result, calculate_total


def create_student(name, registration_number, marks):
    """Build and return a dictionary containing a student's report data."""
    total = calculate_total(marks)
    average = calculate_average(marks)

    return {
        "name": name,
        "registration_number": registration_number,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": calculate_grade(average),
        "result": calculate_result(marks)
    }

