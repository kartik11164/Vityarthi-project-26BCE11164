# System Design

## Architecture diagram

```mermaid
flowchart TD
    User[User in terminal] --> Main[main.py]
    Main --> Menu[Menu module]
    Main --> Validation[Validation module]
    Main --> Student[Student module]
    Student --> Calculator[Calculator module]
    Main --> Reports[Reports module]
    Main --> Storage[Storage module]
    Storage <--> CSV[(students.csv)]
    Main --> Developer[Developer info module]
```

## Workflow diagram

```mermaid
flowchart TD
    A[Start application] --> B[Load saved CSV records]
    B --> C[Show main menu]
    C --> D{User choice}
    D -->|Add student| E[Validate name, registration number, and five marks]
    E --> F[Calculate total, average, grade, and result]
    F --> G[Add record to list]
    G --> C
    D -->|View reports| H[Display all student reports]
    H --> C
    D -->|Search| I[Find registration number and display report]
    I --> C
    D -->|Developer info| J[Display developer details]
    J --> C
    D -->|Save or exit| K[Write records to CSV]
    K --> L{Exit selected?}
    L -->|No| C
    L -->|Yes| M[End]
```

## Use-case diagram

```mermaid
flowchart LR
    User((User))
    Add[Add student record]
    View[View all reports]
    Search[Search student]
    Save[Save records]
    Info[View developer information]
    User --> Add
    User --> View
    User --> Search
    User --> Save
    User --> Info
```

## Component diagram

```mermaid
flowchart LR
    Main[main.py] --> Menu
    Main --> Validators
    Main --> Student
    Student --> Calculator
    Main --> Reports
    Main --> Storage
    Main --> Developer
    Storage --> CSV[CSV File]
```

## Storage design

The program uses one CSV file, `data/students.csv`. Each row stores a student's name, registration number, and five subject/mark pairs. Calculated values are generated again when the file is loaded; this avoids storing duplicate values that could become inconsistent.

| Field group | Description |
|---|---|
| `name`, `registration_number` | Student identity fields |
| `subject_1` to `subject_5` | Names of the five subjects |
| `mark_1` to `mark_5` | Whole-number marks from 0 to 100 |

