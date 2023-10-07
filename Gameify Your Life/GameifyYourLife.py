import tkinter
from tkinter import *
from tkinter.messagebox import showwarning

root = Tk()
root.geometry("960x540")
root.configure(background='gray14')
root.title("To-Do List")
root.resizable = (False, False)

c = Canvas(width= 250, height=480, bg = 'Black')
c.xview_scroll(number= 10, what=['units'])
c.place(x = 0, y = 0)



tasks = []
y_offset = 0

def add_task():
    global y_offset
    task = entry_task.get()
    if task != "":
        task_frame = Frame(c)
        checkbutton = Checkbutton(task_frame, text=task, bg= 'black')
        checkbutton.pack(side=LEFT)
        remove_button = Button(task_frame, text='x', command=lambda t=task: remove_task(t), bg='black')
        remove_button.pack(side=LEFT)
        task_frame.place(x=0, y=y_offset)
        y_offset += 30
        tasks.append({"task": task, "checkbutton": checkbutton, "remove_button": remove_button})
    else:
        showwarning("Warning!", "You must enter a task.")

def remove_task(task_name):
    global y_offset
    for item in tasks:
        if item["task"] == task_name:
            item["checkbutton"].destroy()
            item["remove_button"].destroy()
            tasks.remove(item)
            break

entry_task = Entry(root, width=26)
entry_task.place(x=0, y=485)

plus_icon = PhotoImage(file='Gameify Your Life/plus(50x50).png')
button_add_task = Button(root, image=plus_icon, command=add_task)
button_add_task.place(x=0, y=515)

root.mainloop()
