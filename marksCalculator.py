
import tkinter as tk
from tkinter import messagebox

def calculate_result():
    try:
        # Get marks from input fields
        marks = [
            float(entry1.get()),
            float(entry2.get()),
            float(entry3.get()),
            float(entry4.get()),
            float(entry5.get())
        ]

        # Validate marks
        for mark in marks:
            if mark < 0 or mark > 100:
                messagebox.showerror(
                    "Invalid Marks",
                    "Please enter marks between 0 and 100."
                )
                return

        # Calculate total and percentage
        total = sum(marks)
        percentage = total / 5

        # Calculate grade
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 40:
            grade = "D"
        else:
            grade = "F"

        # Check pass or fail (40 marks in each subject)
        if all(mark >= 40 for mark in marks):
            status = "PASS"
        else:
            status = "FAIL"

        # Display result
        result_label.config(
            text=f"Total Marks: {total:g} / 500\n"
                 f"Percentage: {percentage:.2f}%\n"
                 f"Grade: {grade}\n"
                 f"Result: {status}"
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numbers in all five subjects."
        )


def clear_fields():
    for entry in entries:
        entry.delete(0, tk.END)

    result_label.config(text="Your result will appear here.")


# Create main window
root = tk.Tk()
root.title("Student Marks Calculator")
root.geometry("420x570")
root.resizable(False, False)
root.configure(bg="#EAF2F8")

# Heading
heading = tk.Label(
    root,
    text="Student Marks Calculator",
    font=("Arial", 18, "bold"),
    bg="#EAF2F8",
    fg="#1A5276"
)
heading.pack(pady=20)

# Instructions
instruction = tk.Label(
    root,
    text="Enter marks for 5 subjects (out of 100)",
    font=("Arial", 10),
    bg="#EAF2F8"
)
instruction.pack(pady=5)

# Subject input fields
subjects = [
    "Python",
    "Mathematics",
    "DBMS",
    "Java",
    "DAA"
]

entries = []

for subject in subjects:
    frame = tk.Frame(root, bg="#EAF2F8")
    frame.pack(pady=7)

    label = tk.Label(
        frame,
        text=subject,
        width=15,
        anchor="w",
        font=("Arial", 11),
        bg="#EAF2F8"
    )
    label.pack(side=tk.LEFT, padx=5)

    entry = tk.Entry(frame, width=15, font=("Arial", 11))
    entry.pack(side=tk.LEFT, padx=5)

    entries.append(entry)

# Assign entries to variables
entry1, entry2, entry3, entry4, entry5 = entries

# Calculate button
calculate_button = tk.Button(
    root,
    text="Calculate Result",
    command=calculate_result,
    font=("Arial", 11, "bold"),
    bg="#2874A6",
    fg="white",
    width=20,
    cursor="hand2"
)
calculate_button.pack(pady=15)

# Clear button
clear_button = tk.Button(
    root,
    text="Clear",
    command=clear_fields,
    font=("Arial", 10),
    width=12,
    cursor="hand2"
)
clear_button.pack(pady=3)

# Result display
result_label = tk.Label(
    root,
    text="Your result will appear here.",
    font=("Arial", 12, "bold"),
    bg="white",
    fg="#1A5276",
    width=32,
    height=5,
    relief="groove"
)
result_label.pack(pady=15)

# Start application
root.mainloop()
