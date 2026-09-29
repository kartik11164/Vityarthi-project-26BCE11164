"""Functions that display student records as readable reports."""


def display_student_report(student):
    """Print one detailed student report."""
    print("\n" + "-" * 42)
    print("STUDENT GRADE REPORT")
    print("-" * 42)
    print(f"Name: {student['name']}")
    print(f"Registration Number: {student['registration_number']}")
    print("Subject marks:")
    for item in student["marks"]:
        print(f"  {item['subject']}: {item['mark']}")
    print(f"Total: {student['total']}")
    print(f"Average: {student['average']:.2f}")
    print(f"Grade: {student['grade']}")
    print(f"Result: {student['result']}")


def display_all_reports(students):
    """Print reports for all students in the record list."""
    if len(students) == 0:
        print("\nNo student records are available yet.")
        return

    print(f"\nShowing {len(students)} student report(s):")
    for student in students:
        display_student_report(student)

