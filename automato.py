# imported libraries for python 3 +
import time
import datetime
import webbrowser
import subprocess
import tkinter
from tkinter import messagebox

# You may add a timer delay function for when a file(s) needs to execute. In this example we set a timer for 10 seconds'''
time.sleep(10)

# you may also add a date for when you wish the program to execute. 
# Create a variable (example, longWeekend) and set the date 
longWeekend = datetime.datetime(2017, 7, 4, 0, 0, 0)
while datetime.datetime.now() < longWeekend:
    time.sleep(1)
# the 1 is so the cpu wont waste cpu  processing  

# execute or open up any folder or file on windows, replace with respetive file path
subprocess.Popen('explorer "file path goes here"')
# example - subprocess.Popen('explorer "C:\\Users\\Owner\\Desktop\\folder1"')

# allows for a website(s) to open
webbrowser.open('url address goes here')
# example webbrowser.open('http://www.creativebitstudio.com')

# To display an error, warning or info message to remind you of a task or let you know when a task has been executed
root = tkinter.Tk()
root.withdraw()
# Message boxes to display
messagebox.showerror("Error", "Error message")
# messagebox.showwarning("Warning","Please don't forget to pvr Game of Thrones ")
# messagebox.showinfo("Information","Your task has been activated")



