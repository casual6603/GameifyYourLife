import tkinter
from tkinter import Scrollbar
import tkinter.messagebox
import pickle
from tkinter import * 
from tkinter.ttk import *


 

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")

def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat.")

def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))
 
 
 
 
 
 
 
 
# Main tkinter window
root = tkinter.Tk()
root.geometry("960x540")
root.configure(background='gray14')
root.title("To-Do List")

#creating the photo icons that are used in the bottom left of the screen to add / remove / save / items
minus = PhotoImage (name= 'realrx', file= 'pic.png', height= 20, width= 20)
plus = PhotoImage (name= 'rel', file= 'plus(50x50).png', height= 20, width= 20)
save= PhotoImage (name= 'rel', file= 'plus(50x50).png', height= 20, width= 20)

# Create GUI
frame_tasks = tkinter.Frame(root, width=200, height=540, bg='black')
frame_tasks.place(x=0,y=0)

listbox_tasks = tkinter.Listbox(root, height=200, width=22, bg='grey18')
listbox_tasks.place(x=0,y=0)

entry_task = tkinter.Entry(root, width=21)
entry_task.place(x=0, y= 485)

button_add_task = tkinter.Button(root, image=plus, command=add_task)
button_add_task.place(x=0, y= 512)

button_delete_task = tkinter.Button(root, image=minus, command=delete_task, bg='black')
button_delete_task.place(x = 40, y = 512)

button_save_tasks = tkinter.Button(root, image=save,  width=22, command=save_tasks)
button_save_tasks.place(x=80, y= 512)








root.mainloop()





