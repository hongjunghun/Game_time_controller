from tkinter import *
from function import Timing
import time

def save():
    hour = int(ent1.get())
    minute = int(ent2.get())
    second = int(ent3.get())
    control.input_wanting_time(hour, minute, second, value.get())


control = Timing()

window = Tk()
window.geometry("275x150")
window.resizable(height=False, width=False)
window.title("TIME CONTROLL")

# input hour
lab2 = Label(window, text="hour"); lab2.grid(row=0, column=1)
ent1 = Entry(); ent1.grid(row=0, column=0)

# input minute
lab3 = Label(window, text="minute");lab3.grid(row=1,column=1)
ent2 = Entry(); ent2.grid(row=1, column=0)

# input second
lab4 = Label(window, text="second"); lab4.grid(row=2, column=1)
ent3 = Entry(); ent3.grid(row=2, column=0)

lab5 = Label(window, text=".exe file"); lab5.grid(row=3, column=1)

options = ["RobloxPlayerBeta.exe", "OtherProgram.exe(developing..)", "AnotherApp.exe(developing..)"]
value = StringVar(window)
value.set(options[0])

dropdown = OptionMenu(window, value, *options)
dropdown.grid(row=3, column=0)

def update_clock():
    now = time.localtime()
    h = now.tm_hour
    m = now.tm_min
    s = now.tm_sec
    lab.config(text=f"current time : {h:02d}:{m:02d}:{s:02d}")
    window.after(1000, update_clock)

# current time
lab = Label(window, font=("Arial", 14)); lab.grid(row=4, column=0, padx=15)

# submit button
btn = Button(window, text="OK", command=save)
btn.grid(row=5, column=0)

update_clock()

window.mainloop()
