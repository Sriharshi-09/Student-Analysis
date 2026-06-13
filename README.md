# Student Performance Analysis System

## Project Overview

The Student Performance Analysis System is a Python-based application that reads student data from a CSV file, performs academic performance analysis, and generates visualizations. The project uses Pandas and NumPy for data processing and Matplotlib and Seaborn for data visualization.

## Features

* Read student data from a CSV file
* Calculate Total Marks
* Calculate Average Marks
* Calculate Percentage
* Assign Grades Automatically
* Identify Topper(s)
* Identify Failed Students
* Perform Statistical Analysis using NumPy
* Generate Graphical Visualizations
* Export Processed Report to CSV

## Technologies Used

* Python 3.x
* Pandas
* NumPy
* Matplotlib
* Seaborn

## Project Structure

```text
Student_Performance_Analysis/
│
├── students.csv
├── student_analysis.py
├── student_report.csv
├── percentage_distribution.png
├── student_percentages.png
├── grade_distribution.png
└── README.md
```

## Dataset Format

The input CSV file should contain the following columns:

```csv
StudentID,Name,Maths,Science,English
101,Alice,85,90,88
102,Bob,65,70,60
```

## Installation

Install the required libraries using pip:

```bash
pip install pandas numpy matplotlib seaborn
```

## How to Run

1. Place the `students.csv` file in the project directory.
2. Open Terminal or Command Prompt.
3. Navigate to the project folder.
4. Execute the Python script:

```bash
python student_analysis.py
```

## Output Generated

The application generates:

* Student Report with Total, Average, Percentage, and Grade
* Topper Details
* Failed Student List
* Statistical Analysis Results
* Percentage Distribution Graph
* Student Percentage Comparison Chart
* Grade Distribution Pie Chart

## Grading Criteria

| Percentage   | Grade |
| ------------ | ----- |
| 90 and above | A+    |
| 80 - 89      | A     |
| 70 - 79      | B     |
| 60 - 69      | C     |
| 50 - 59      | D     |
| Below 50     | F     |

## Sample Output

```text
===== TOPPER =====
Name: Jack
Percentage: 97.67

===== FAILED STUDENTS =====
David
Henry
```

## Learning Outcomes

This project helps in understanding:

* Data Analysis using Pandas
* Numerical Computations using NumPy
* CSV File Handling
* Data Visualization
* Python Functions and Conditional Statements
* Report Generation

## Conclusion

The Student Performance Analysis System demonstrates the practical application of Python for educational data analysis. It provides meaningful insights into student performance and presents results through both tabular and graphical formats.
