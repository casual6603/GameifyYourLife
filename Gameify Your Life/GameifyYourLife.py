from tkinter import *
from tkinter.messagebox import showwarning
import matplotlib as plt
import threading #for timer


root = Tk()
root.geometry("1920x1080")
root.title("Gameify Your Life")

Top_frame = Canvas(root, width = 1920, height= 50, bg = "orange") 
Top_frame.pack(side=TOP)#dont forget to find a way to make this have a ppicture as a background, similar to the profile banner on youtube

Name_module = Label(root, text=  "Hello, 'Name'", font=("arial",25),padx=15,pady=15 ) #3find way to make name dynamic
Name_module.place(x = 0, y = 53)


Todays_goals = Canvas(root, width = 500, height = 400, bg = "orange")
Todays_goals.place(x=0, y= 100)

This_weeks_goals = Canvas(root, width = 500, height = 400, bg = "orange")
This_weeks_goals.place(x=500, y= 100)

This_months_goals = Canvas(root, width = 500, height = 400, bg = "orange")
This_months_goals.place(x=1000, y= 100)

Goals_canvas_text = Label(root, text=  "Goals Canvas", font=("arial",25),padx=15,pady=15 ) #3find way to make name dynamic
Goals_canvas_text.place(x = 550, y= 540)

Goals_canvas = Canvas(root, width = 1500, height = 400, bg = "orange")
Goals_canvas.place(x=0, y=600)


#ay 3rd times the charm right

"""
import tkinter
from tkinter import *
from tkinter.messagebox import showwarning
import matplotlib as plt

root = Tk()
root.resizable(False,False)
root.geometry("960x540")
root.title("To-Do List")


scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

checklist = Text(root, width=40, height= 40,  bg='red')
checklist.place(x = 0, y= 0)
checklist.lower()

list_lower = Canvas(root, width= 40, height= 40)
list_lower.place (x= 0, y= 0)




input_area = Canvas(root, width = 145, height= 100, bg= 'black')
input_area.place(x = 0, y= 495)


def new_window():
    Canvas(list_lower, width= 
    282 , height= 100, bg= 'black').pack(side=RIGHT)
def new_checkbutton():
    i = ent.get()
    if i != "":
        checkbutton = Checkbutton(checklist, text=i, bg= 'red')    
        checklist.window_create("end", window=checkbutton)
        checklist.insert("end", "\n")
    else :
        showwarning("Warning!", "You must enter a task.")
        
input = Button(input_area, text= "realrx", bg= "red",  command= new_checkbutton)
input.pack(expand= 10)


Button(root, text= "realrx", bg= "red",  command= new_window).pack(expand= 10)

ent = Entry(input_area)
ent.pack()

checklist.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=checklist.yview)

# disable the widget so users can't insert text into it
checklist.configure(state="disabled")

root.mainloop()

"""


#tasks = []
#y_offset = 0

#def add_task():
    #global y_offset
        #ewllsdfjklasdfj adfasdf;lkj sf
# task = entry_task.get()
#    if task != "":
 #       task_frame = Frame(checklist)
#        checkbutton = Checkbutton(task_frame, text=task)
#        checklist.insert(side=LEFT)
#        remove_button = Button(task_frame, text='x', command=lambda t=task: remove_task(t))
#        remove_button.pack(side=LEFT)
#        task_frame.place(x=10, y=y_offset)
#        y_offset += 30
#        tasks.append({"task": task, "checkbutton": checkbutton, "remove_button": remove_button})
#    else:
#        showwarning("Warning!", "You must enter a task.")

#def remove_task(task_name):
#    global y_offset
#    for item in tasks:
#        if item["task"] == task_name:
#            item["checkbutton"].destroy()
#            item["remove_button"].destroy()
#            tasks.remove(item)
#            break

#entry_task = Entry(root, width=21)
#entry_task.place(x=0, y=485)

#plus_icon = PhotoImage(file='Gameify Your Life/plus(50x50).png')
#button_add_task = Button(root, image=plus_icon, command=add_task)
#button_add_task.place(x=0, y=515)

root.mainloop()
