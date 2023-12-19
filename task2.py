#!python3

"""
##### Task 2 Calculator
Create a simple app that allows you to do a calculation with an arithmetic operation.  You will need a spinbox between 2 entry boxes.  The entryboxes are where you should be entering your numbers, and the spinbox should be the operator.  You will need a button to do the calculation.  You can modify your assignment from A500 for this.
"""
import tkinter as tk

win = tk.Tk()
win.title("Simple Calculator")
win.geometry("135x150")
win.attributes('-topmost',True)

entry1=tk.Entry(win)
entry1.place(x=5,y=1)
entry2=tk.Entry(win)
entry2.place(x=5,y=50)

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operator = operators[operator_var.get()]
        result = eval(f"{num1} {operator} {num2}")
        resultlabel.config(text=f"Result: {result}")
    except ValueError:
        resultlabel.config(text="Enter valid numbers")
    except ZeroDivisionError:
        resultlabel.config(text="Can't divide by zero")


operators={"+": "+", "-": "-", "*": "*", "/": "/"}
operator_var = tk.StringVar()
operatorspinbox =tk.Spinbox(win, values=list(operators.keys()),textvariable=operator_var)
operatorspinbox.place(x=1,y=30)
 
button=tk.Button(win, text="Calculate", command=calculate)
button.place(x=33, y=80)

resultlabel=tk.Label(win, text="result: ")
resultlabel.place(x=40,y=120)


win.mainloop()