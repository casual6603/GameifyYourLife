import tkinter
from tkinter import Scrollbar
import tkinter.messagebox
import pickle
from tkinter import * 
from tkinter.ttk import *
from random import randint


# Main tkinter window
root = Tk()
root.geometry("960x540")
root.configure(background='gray14')
root.title("To-Do List")


task = StringVar()

y_offset = 0

def checkbox(f, name1, y_location):
    name1 = Checkbutton(root, text = name1)
    name1.place(x= 10, y = y_location)
    
    
tasks = []

def add_task():
    global y_offset
    global task
    real = Frame(root)
    task = entry_task.get()
    if task != "":
        checkbutton = Checkbutton(root, text=task)
        checkbutton.place(x=10, y=y_offset)
        y_offset = y_offset + 20
        tasks.append({"task": task, "checkbutton": checkbutton})
        xy = Button(root, text='x', command=lambda t=task: remove_task(t), width=1)
        xy.place(x=60, y=y_offset)

# Function to remove a task and its checkbutton
def remove_task(task_name):
    for item in tasks:
        if item["task"] == task_name:
            item["checkbutton"].destroy()
            tasks.remove(item)
            item["xy"].destroy()
            break
            
        
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")




 
 
#creating the photo icons that are used in the bottom left of the screen to add / remove / save / items
minus = PhotoImage (name= 'realrx', file= 'Gameify Your Life/plus(50x50).png', height= 20, width= 20)
plus = PhotoImage (name= 'rel', file= 'Gameify Your Life/plus(50x50).png', height= 20, width= 20)
save= PhotoImage (name= 'rel', file= 'Gameify Your Life/plus(50x50).png', height= 20, width= 20)
load= PhotoImage (name= 'rel', file= 'Gameify Your Life/plus(50x50).png', height= 20, width= 20)

# Create GUI
frame_tasks = tkinter.Frame(root, width=200, height=540, bg='black')
frame_tasks.place(x=0,y=0)

entry_task = tkinter.Entry(root, width=21)
entry_task.place(x=0, y= 485)

button_add_task = tkinter.Button(root, image=plus, command=(add_task))
button_add_task.place(x=0, y= 515)





root.mainloop()
