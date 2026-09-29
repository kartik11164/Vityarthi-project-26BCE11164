# Project Statement: Student Grade Calculator

## Problem statement

Teachers and students often need a quick and consistent way to convert subject marks into a total, average, grade, and final result. Calculating these values manually can take time and can lead to mistakes. This project provides a simple command-line solution for storing student marks and generating clear grade reports.

## Scope

The application records marks for five subjects for each student. It calculates the total, average, letter grade, and pass/fail result. It can display all reports, search for a report using a registration number, and save data in a CSV file so records remain available after the program closes.

## Target users

- First-semester students who want to understand their grade calculation
- Teachers who need a small offline tool for entering marks
- Beginners learning Python lists, dictionaries, loops, conditions, functions, and file handling

## High-level features

1. **Student record management:** add student details and five subject marks.
2. **Grade processing:** calculate total, average, grade, and result.
3. **Reporting:** view every report or search for one student.
4. **Data storage:** load and save records in CSV format.
5. **Developer information:** show the project developer's details through the menu.

## Non-functional requirements

1. **Usability:** the numbered terminal menu should be clear for first-time users.
2. **Reliability:** marks and required details are validated before a record is created.
3. **Maintainability:** each responsibility is stored in a separate Python module.
4. **Performance:** the application should respond quickly for a small class-size list of records.
5. **Resource efficiency:** it uses only Python's standard library and a small CSV file.

