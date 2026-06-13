import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read CSV File
df = pd.read_csv("students.csv")

# Calculate Total Marks
df["Total"] = df["Maths"] + df["Science"] + df["English"]

# Calculate Average
df["Average"] = df["Total"] / 3

# Calculate Percentage
df["Percentage"] = (df["Total"] / 300) * 100

# Grade Calculation
def calculate_grade(percent):
    if percent >= 90:
        return "A+"
    elif percent >= 80:
        return "A"
    elif percent >= 70:
        return "B"
    elif percent >= 60:
        return "C"
    elif percent >= 50:
        return "D"
    else:
        return "F"

df["Grade"] = df["Percentage"].apply(calculate_grade)

# Identify Toppers
topper = df.loc[df["Percentage"].idxmax()]

# Failed Students
failed_students = df[
    (df["Maths"] < 40) |
    (df["Science"] < 40) |
    (df["English"] < 40)
]

print("\n===== STUDENT REPORT =====")
print(df)

print("\n===== TOPPER =====")
print(topper)

print("\n===== FAILED STUDENTS =====")
print(failed_students[["StudentID", "Name"]])

# NumPy Analysis
marks_array = df[["Maths", "Science", "English"]].values

print("\n===== NUMPY ANALYSIS =====")
print("Mean Marks:", np.mean(marks_array))
print("Highest Marks:", np.max(marks_array))
print("Lowest Marks:", np.min(marks_array))
print("Standard Deviation:", np.std(marks_array))

# Save Updated Report
df.to_csv("student_report.csv", index=False)

# Visualization 1: Percentage Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["Percentage"], bins=5, kde=True)
plt.title("Percentage Distribution")
plt.savefig("percentage_distribution.png")
plt.show()

# Visualization 2: Student Percentages
plt.figure(figsize=(10,5))
sns.barplot(x="Name", y="Percentage", data=df)
plt.title("Student Percentage Comparison")
plt.xticks(rotation=45)
plt.savefig("student_percentages.png")
plt.show()

# Visualization 3: Grade Distribution
plt.figure(figsize=(6,6))
df["Grade"].value_counts().plot.pie(
    autopct='%1.1f%%'
)
plt.title("Grade Distribution")
plt.ylabel("")
plt.savefig("grade_distribution.png")
plt.show()

print("\nAnalysis Completed Successfully!")