"""
##### Task 1 Select birthdate.
Create an application that allows the user to select the month, day and year of their birthdate. You will need 3 separate entries: month,day, year.

You are responsible for designing your GUI.  You may use the pack, grid or place methods for doing so, but your GUI layout should be organized and visually appealing.

Display the results of their selection in an entry box in the widget.

Extra: Can you create some of the lists of values dynamically instead of explicitly listing them all?
"""
import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.attributes('-topmost',True)
win.geometry("300x200")


l1 = tkinter.Label(win,text="Select day ")
l2 = tkinter.Label(win,text="Select month ")
l3 = tkinter.Label(win,text="Select year ")
l4 = tkinter.Label(win,text="Your Birthday is")

c1 = ttk.Spinbox(win,values=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],width=10)
c2 = ttk.Spinbox(win,values=["January","February","March","April", "May","June","July","August","September","October","November","December"],width=10)
c3 = ttk.Spinbox(win,from_ = 1920, to = 2023,width=10)
c1.set(1)
c2.set("January")
c3.set(2000)

eoutput = tkinter.StringVar()

def clickFunction(event):
    a = c1.get()
    b = c2.get()
    c = c3.get()
    answer = (f"{b} {a}, {c}")
    a_entry.delete(0,tkinter.END)
    a_entry.insert(0,answer)

b = tkinter.Button(win,text="Click to confirm")
b.bind("<Button>",clickFunction)


l1.place(x=50,y=5)
l2.place(x=50,y=25)
l3.place(x=50,y=45)
b.place(x=100,y=70)
l4.place(x=1,y=98)

c1.place(x=140,y=5)
c2.place(x=140,y=25)
c3.place(x=140,y=45)

a_entry = tkinter.Entry(win, width=20, textvariable=eoutput)
a_entry.place(x=92,y=98)

win.mainloop()