"""Entry point for the Student Grade Calculator application."""

from app.developer import show_developer_info
from app.menu import show_main_menu
from app.reports import display_all_reports, display_student_report
from app.storage import load_students, save_students
from app.student import create_student
from app.validators import get_menu_choice, get_non_empty_text


DATA_FILE = "data/students.csv"


def registration_exists(students, registration_number):
    """Return True if a registration number is already in the records."""
    for student in students:
        if student["registration_number"].lower() == registration_number.lower():
            return True
    return False


def add_student(students):
    """Collect one student's details and add the record to the list."""
    print("\n--- Add Student ---")
    name = get_non_empty_text("Enter student name: ")
    registration_number = get_non_empty_text("Enter registration number: ")

    if registration_exists(students, registration_number):
        print("A student with this registration number already exists.")
        return

    marks = []
    subject_number = 1
    while subject_number <= 5:
        subject_name = get_non_empty_text(f"Enter name of subject {subject_number}: ")
        mark = get_menu_choice(f"Enter marks for {subject_name} (0-100): ", 0, 100)
        marks.append({"subject": subject_name, "mark": mark})
        subject_number += 1

    student = create_student(name, registration_number, marks)
    students.append(student)
    print(f"Student record for {name} added successfully.")


def search_student(students):
    """Find a student by registration number and display the report."""
    print("\n--- Search Student ---")
    registration_number = get_non_empty_text("Enter registration number: ")

    for student in students:
        if student["registration_number"].lower() == registration_number.lower():
            display_student_report(student)
            return

    print("No student was found with that registration number.")


def run_application():
    """Run the main menu until the user chooses to exit."""
    students = load_students(DATA_FILE)
    print("Welcome to the Student Grade Calculator")

    while True:
        show_main_menu()
        choice = get_menu_choice("Choose an option (1-6): ", 1, 6)

        if choice == 1:
            add_student(students)
        elif choice == 2:
            display_all_reports(students)
        elif choice == 3:
            search_student(students)
        elif choice == 4:
            save_students(DATA_FILE, students)
        elif choice == 5:
            show_developer_info()
        else:
            save_students(DATA_FILE, students)
            print("Thank you for using the Student Grade Calculator.")
            break


if __name__ == "__main__":
    run_application()

