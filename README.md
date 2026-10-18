
Expense Tracker — Python Project

A simple, menu-driven Expense Tracker developed using Python as the final project for the InternNova Python Programming Internship — Week 6.

1. Project Description

The Expense Tracker is a command-line application that helps users record and manage daily expenses. Users can add expenses, view saved records, and calculate their total spending.

The application stores expense records in a CSV file, allowing previously saved records to be loaded when the program starts again.

2. Project Objectives

- Apply Python programming concepts to a practical project.
- Develop a menu-driven application.
- Record and display expense details.
- Calculate total expenses.
- Store data permanently using CSV file handling.
- Validate user input and handle common errors.
- Implement object-oriented programming concepts.
- Use Git and GitHub for version control and project management.

3. Features

- Add Expense: Record the category, description, and amount.
- View Expenses: Display all saved expense records.
- Calculate Total: Calculate and display total spending.
- CSV Persistence: Save expense records to "expenses.csv".
- Automatic Loading: Load previously saved records when the program starts.
- Input Validation: Reject empty categories, empty descriptions, and non-positive amounts.
- Exception Handling: Handle invalid numeric input and common file errors.
- Date Tracking: Automatically record the current date for new expenses.
- Menu-Driven Interface: Navigate through the application using numbered options.

4. Technologies Used

Technology| Purpose
Python 3| Application development
"csv" module| Reading and writing expense records
"datetime" module| Recording expense dates
"os" module| Checking whether the CSV file exists
Git| Version control
GitHub| Online source-code hosting
VS Code or IDLE| Writing and executing Python code

5. Python Concepts Used

This project demonstrates the following concepts:

1. Variables and Data Types: Store expense details and amounts.
2. Input and Output: Accept user input and display results.
3. Type Casting: Convert the expense amount to a floating-point number.
4. Conditional Statements: Handle menu choices and validate input.
5. Loops: Keep the application running until the user exits.
6. Functions and Methods: Organize application operations into reusable methods.
7. Classes and Objects: Use "Expense" and "ExpenseTracker" classes.
8. Constructor: Initialize expense details and tracker data.
9. Encapsulation: Store the amount in the private attribute "__amount" and access it through a getter method.
10. Lists: Maintain expense objects in memory.
11. File Handling: Read and write expense records.
12. Exception Handling: Handle invalid amounts and common file errors.
13. Standard Library Modules: Use "csv", "datetime", and "os".
14. Version Control: Track project changes using Git and share the project through GitHub.

6. Project Structure

Expense-Tracker/
│
├── main.py
├── README.md
├── requirements.txt
├── expenses.csv
├── screenshots/
│   ├── main_menu.png
│   ├── add_expense.png
│   ├── view_expenses.png
│   └── total_expenses.png
│
└── docs/
    └── Week_6_Project_Report.md

File descriptions:

- "main.py": Main Python application.
- "README.md": Project documentation.
- "requirements.txt": Dependency information.
- "expenses.csv": Stores saved expense records; created when an expense is successfully saved.
- "screenshots/": Contains screenshots of actual program execution.
- "docs/": Contains the project report.

The CSV file and screenshot files may not exist until you create or generate them. Include only files that are actually present in your repository.

7. Prerequisites

Before running the application, ensure that:

- Python 3 is installed on your computer.
- A code editor or terminal is available.
- You have downloaded or cloned the project repository.

No external Python packages are required because the project uses Python's standard library.

8. Installation and Setup

Step 1: Download the Project

Download the repository from GitHub or clone it using:

git clone https://github.com/YOUR_USERNAME/Expense-Tracker.git

Replace "YOUR_USERNAME" with your actual GitHub username.

Step 2: Open the Project Folder

cd Expense-Tracker

Step 3: Verify Python Installation

python --version

On some systems, use:

python3 --version

Step 4: Run the Application

python main.py

If your system uses "python3", run:

python3 main.py

9. How to Use the Application

When the program starts, the following menu appears:

==============================
       EXPENSE TRACKER
==============================
1. Add Expense
2. View Expenses
3. Calculate Total
4. Exit
==============================
Enter your choice:

Option 1: Add Expense

Enter the category, description, and amount.

Example:

--- Add Expense ---
Enter category: Food
Enter description: Lunch
Enter amount: 150
Expense added successfully!

Option 2: View Expenses

Display all saved expense records, including their dates, categories, descriptions, and amounts.

Option 3: Calculate Total

Calculate the total amount of all loaded expense records.

Example:

Total Expenses: Rs. 150.00

Option 4: Exit

Exit the application safely.

10. Sample Data

Example expense records:

Date| Category| Description| Amount
2026-10-18| Food| Lunch| ₹150.00
2026-10-18| Travel| Bus Ticket| ₹40.00
2026-10-18| Education| Notebook| ₹60.00

Example total: ₹250.00

These are illustrative sample records. The application uses the current date for newly added expenses. Use sample data when demonstrating the project.

11. Error Handling

The application handles common errors, including:

- Entering text instead of a numeric amount.
- Entering zero or a negative amount.
- Leaving the category or description empty.
- Selecting an invalid menu option.
- Encountering common file-access or CSV-data errors.

Appropriate messages are displayed to help the user understand the problem.

12. Testing

The application should be tested using the following scenarios:

Test| Expected Result
Add a valid expense| Expense is saved successfully
View saved expenses| Saved records are displayed
Calculate total| Correct total is displayed
Enter an invalid amount| Error message appears
Enter a zero or negative amount| Amount is rejected
Leave required fields empty| Input is rejected
Enter an invalid menu choice| Invalid-choice message appears
Restart after saving an expense| Saved records are loaded again

Run each test and verify the actual result before reporting it as passed.

13. Limitations

- The application uses a command-line interface.
- It does not currently provide a graphical user interface.
- It does not include monthly reports or category-wise summaries.
- It does not provide budget alerts.
- Expense records are stored locally in a CSV file.
- It does not include user accounts or multi-user access.

14. Future Improvements

Possible enhancements include:

- Monthly and yearly expense reports.
- Category-wise expense analysis.
- Search and filter functionality.
- Budget limits and spending alerts.
- Graphs and charts for expense visualization.
- A graphical user interface.
- Exporting reports to PDF or Excel.
- Improved backup and data-recovery features.

15. Version Control with Git

The project can be tracked and uploaded to GitHub using:

git init
git add main.py README.md requirements.txt
git commit -m "Initial Expense Tracker project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/Expense-Tracker.git
git push -u origin main

If the repository has already been initialized and connected, do not repeat "git init" or "git remote add origin" unnecessarily. Commit and push subsequent changes using:

git add .
git commit -m "Update Expense Tracker project"
git push

Before using "git add .", check "git status" and ensure that personal or confidential data will not be uploaded.

16. Screenshots

Add genuine screenshots of the following application features to the "screenshots/" folder:

1. Main menu.
2. Adding an expense.
3. Viewing saved expenses.
4. Calculating total expenses.
5. Handling invalid input.
6. GitHub repository showing the uploaded files.

17. Author Information

Student Name: Kalpesh

Internship Organization: InternNova

Internship Domain: Python Programming

Assignment: Week 6 — Git, GitHub & Final Python Project

Project Title: Expense Tracker — A Python-Based Expense Management System

GitHub Repository: Add your actual repository URL here.

18. Conclusion

The Expense Tracker is a practical Python project that demonstrates fundamental programming, object-oriented programming, CSV file handling, input validation, and exception handling.

The project also introduces version control using Git and source-code hosting through GitHub. It provides a foundation for developing more advanced expense management applications with reporting, visualization, and budget management features.

---

Output :

```python
PS D:\Data\Projects\InterNova> python -u "d:\Data\Projects\InterNova\Week-6\Expense-Tracker\main.py"

==============================
       EXPENSE TRACKER
==============================
1. Add Expense
2. View Expenses
3. Calculate Total
4. Exit
==============================
Enter your choice: 1

--- Add Expense ---
Enter category: Food
Enter description: Lunch
Enter amount: 150
Expense added successfully!

==============================
       EXPENSE TRACKER
==============================
1. Add Expense
2. View Expenses
3. Calculate Total
4. Exit
==============================
Enter your choice: 1

--- Add Expense ---
Enter category: Travel
Enter description: Bus Ticket
Enter amount: 40
Expense added successfully!

==============================
       EXPENSE TRACKER
==============================
1. Add Expense
2. View Expenses
3. Calculate Total
4. Exit
==============================
Enter your choice: 2

--- All Expenses ---

Expense 1:
Date: 2026-10-18 | Category: Food | Description: Lunch | Amount: Rs. 150.00

Expense 2:
Date: 2026-10-18 | Category: Travel | Description: Bus Ticket | Amount: Rs. 40.00

==============================
       EXPENSE TRACKER
==============================
1. Add Expense
2. View Expenses
3. Calculate Total
4. Exit
==============================
Enter your choice: 3

Total Expenses: Rs. 190.00

==============================
       EXPENSE TRACKER
==============================
1. Add Expense
2. View Expenses
3. Calculate Total
4. Exit
==============================
Enter your choice: 4
Thank you for using Expense Tracker!

```