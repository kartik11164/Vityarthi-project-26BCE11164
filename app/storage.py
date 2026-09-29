"""CSV storage functions for student records."""

import csv
import os

from app.student import create_student


FIELD_NAMES = [
    "name", "registration_number", "subject_1", "mark_1", "subject_2", "mark_2",
    "subject_3", "mark_3", "subject_4", "mark_4", "subject_5", "mark_5"
]


def load_students(filename):
    """Load saved records; return an empty list when the file is unavailable."""
    students = []
    if not os.path.exists(filename):
        return students

    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                marks = []
                subject_number = 1
                while subject_number <= 5:
                    marks.append({
                        "subject": row[f"subject_{subject_number}"],
                        "mark": int(row[f"mark_{subject_number}"])
                    })
                    subject_number += 1
                students.append(create_student(row["name"], row["registration_number"], marks))
    except (OSError, ValueError, KeyError):
        print("Saved data could not be read. Starting with an empty record list.")
        return []

    return students


def save_students(filename, students):
    """Save all student records to a CSV file."""
    folder_name = os.path.dirname(filename)
    if folder_name:
        os.makedirs(folder_name, exist_ok=True)

    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELD_NAMES)
            writer.writeheader()
            for student in students:
                row = {
                    "name": student["name"],
                    "registration_number": student["registration_number"]
                }
                subject_number = 1
                for item in student["marks"]:
                    row[f"subject_{subject_number}"] = item["subject"]
                    row[f"mark_{subject_number}"] = item["mark"]
                    subject_number += 1
                writer.writerow(row)
        print("Records saved successfully.")
    except OSError:
        print("Records could not be saved. Check folder permissions and try again.")

