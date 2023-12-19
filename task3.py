#!python3

"""
##### Task 3 tKinter Compound Interest 
Create an application to calculate the final value of a compount interest value problem.  Recall that the final value can be calculated with:

A = P(1+r/n)^(n*t) where:
P = Principal (amount of the initial investment)
r = Interest rate as a decimal (4% has r = 0.04)
n = Number of compounding periods in a year (monthly n = 12, daily n=365)
t = number of years

You should decide which values should have regular entry widgets, comboboxes or spinboxes.  You will need a label or entry box to show your result.
"""
import tkinter as tk
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operator = operators[operator_var.get()]
        result = eval(f"{num1} {operator} {num2}")
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Enter valid numbers")
    except ZeroDivisionError:
        result_label.config(text="Cannot divide by zero")

# Create the main window
app = tk.Tk()
app.title("Simple Calculator")

# Entry boxes
entry1 = tk.Entry(app)
entry1.pack(pady=10)
entry2 = tk.Entry(app)
entry2.pack(pady=10)

# Spinbox for operators
operators = {"+": "+", "-": "-", "*": "*", "/": "/"}
operator_var = tk.StringVar()
operator_spinbox = tk.Spinbox(app, values=list(operators.keys()), textvariable=operator_var)
operator_spinbox.pack(pady=10)

# Button to perform calculation
calculate_button = tk.Button(app, text="Calculate", command=calculate)
calculate_button.pack(pady=10)

# Result label
result_label = tk.Label(app, text="Result: ")
result_label.pack(pady=10)

# Run the application
app.mainloop()
