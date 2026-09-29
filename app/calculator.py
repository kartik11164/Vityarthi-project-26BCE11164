"""Functions for calculating totals, averages, grades, and results."""


def calculate_total(marks):
    """Return the sum of all subject marks."""
    total = 0
    for item in marks:
        total += item["mark"]
    return total


def calculate_average(marks):
    """Return the average mark, or 0 when no marks are supplied."""
    if len(marks) == 0:
        return 0
    return calculate_total(marks) / len(marks)


def calculate_grade(average):
    """Return a letter grade based on the average mark."""
    if average >= 90:
        return "A+"
    if average >= 80:
        return "A"
    if average >= 70:
        return "B+"
    if average >= 60:
        return "B"
    if average >= 50:
        return "C"
    if average >= 40:
        return "D"
    return "F"


def calculate_result(marks):
    """Return Pass only if every subject has a mark of at least 40."""
    for item in marks:
        if item["mark"] < 40:
            return "Fail"
    return "Pass"

