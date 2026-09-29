# Student Grade Calculator

A beginner-friendly command-line Python application for recording student marks, calculating grades, viewing reports, searching for students, and saving records to a CSV file.

## Features

- Add a student and marks for five subjects
- Automatically calculate total, average, grade, and pass/fail result
- View all saved student reports
- Search for a student by registration number
- Save records to, and load records from, a CSV file
- View developer information from the main menu

## Technologies used

- Python 3
- Python standard library only (`csv` and `os`)

## Project structure

```
student-grade-calculator/
|-- app/
|   |-- calculator.py       # Grade calculation rules
|   |-- developer.py        # Developer information
|   |-- menu.py             # Console menu display
|   |-- reports.py          # Report formatting and display
|   |-- storage.py          # CSV save and load operations
|   |-- student.py          # Student record creation
|   `-- validators.py       # User-input validation
|-- data/                   # Created student data is saved here
|-- docs/
|   `-- design.md           # Architecture and workflow diagrams
|-- tests/
|   `-- test_calculator.py  # Validation tests
|-- main.py                 # Application entry point
|-- README.md
`-- statement.md
```

## Requirements

- Python 3.8 or newer

No external packages need to be installed.

## Setup and run

1. Download or clone this repository.
2. Open a terminal in the repository folder.
3. Check that Python is installed:

   ```bash
   python --version
   ```

4. Run the program:

   ```bash
   python main.py
   ```

   If your computer uses `python3`, run `python3 main.py` instead.

5. Choose an option from the numbered menu. Student records are saved automatically to `data/students.csv` when you exit.

## How grades are calculated

Each student receives a mark from 0 to 100 in five subjects. The program calculates the average and assigns a grade:

| Average | Grade |
|---:|:---|
| 90-100 | A+ |
| 80-89 | A |
| 70-79 | B+ |
| 60-69 | B |
| 50-59 | C |
| 40-49 | D |
| Below 40 | F |

A student passes only when every subject mark is at least 40.

## Testing

Run the built-in validation tests from the repository root:

```bash
python -m unittest discover -s tests -v
```

## Error handling

- Blank names and registration numbers are rejected.
- Marks must be whole numbers from 0 to 100.
- Duplicate registration numbers are not allowed.
- A missing or invalid data file does not stop the application from running.

