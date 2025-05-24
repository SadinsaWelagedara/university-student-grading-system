# University Students Grading System

This Python based application allows users to predict student academic progression outcomes based on credit values, using predefined university rules.

# Features

### Part 1: Progression Outcome Prediction
- Prompts user to input credits for **Pass**, **Defer**, and **Fail**
- Validates:
  - Correct **integer** input
  - Credit values must be one of: `0, 20, 40, 60, 80, 100, 120`
  - Total credits must equal `120`
- Displays appropriate outcome:
  - `Progress`
  - `Progress (module trailer)`
  - `Do not Progress – module retriever`
  - `Exclude`

### Multiple Student Records
- Allows repeated data entry for multiple students
- User can quit using `'q'` or continue using `'y'`

### Part 1D: Outcome Histogram
- Generates a histogram (graphical bar chart) using the `graphics.py` module
- Shows the total count for each outcome category

### Part 2: List Storage
- Stores each student’s progression result and credit breakdown in a **list**
- Prints all stored records in the following format :
  `Progress - 120, 0, 0 `
  `Module retriever - 80, 20, 20 `
