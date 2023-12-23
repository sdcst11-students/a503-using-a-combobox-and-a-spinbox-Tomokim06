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

win = tk.Tk()
win.title("Calculate Interest")
win.geometry("220x180")
win.attributes('-topmost',True)

def calculate():
    P = float(initialentry.get())
    R = float(interestentry.get())
    r = R/100
    t = float(years.get())
    N = compoundingperiods.get()
    if N == "Monthly":
        n=2
    if N == "Quarterly":
        n=4
    if N == "Semi-Annually":
        n=2
    if N == "Monthly":
        n=1
    A = round((P*(1+r/n)**(n*t)),2)
    result.delete(0,tk.END)
    result.insert(0,A)

#TEXTS     
initial=tk.Label(win, text="Inivital Investment: ")
interest=tk.Label(win, text="Interest Rate: ")
compounded=tk.Label(win, text="Interest is compounded: ")
years=tk.Label(win, text="Years to grow: ")
resultlabel=tk.Label(win, text="result: ")
percentage=tk.Label(win, text="%")
dollarsign=tk.Label(win, text="$")
dollarsign2=tk.Label(win, text="$")

initial.place(x=1,y=1)
interest.place(x=1,y=26)
compounded.place(x=1,y=51)
years.place(x=1,y=76)
resultlabel.place(x=1,y=150)
percentage.place(x=94,y=26)
dollarsign.place(x=140,y=1)
dollarsign2.place(x=164,y=150)

#ENTRYBOXES
initialentry=tk.Entry(win,width=5)
initialentry.place(x=107,y=1)
interestentry=tk.Entry(win,width=3)
interestentry.place(x=75,y=26)

result=tk.Entry(win,text="roll result")
result.place(x=42,y=150)

#SPINBOXES
compoundingperiods=tk.Spinbox(win, values=["Monthly","Quarterly","Semi-Annually","Yearly"],width=10)
compoundingperiods.place(x=135,y=51)
years=tk.Spinbox(win, values=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50],width=2)
years.place(x=82,y=76)

#BUTTONS
button=tk.Button(win, text="Calculate", command=calculate)
button.place(x=1, y=110)

win.mainloop()