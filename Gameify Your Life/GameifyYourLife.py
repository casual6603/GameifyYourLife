import tkinter
from tkinter import *
from tkinter.messagebox import showwarning


root = Tk()
root.resizable(False,False)
root.geometry("960x540")
root.title("To-Do List")

scrollbar = Scrollbar(root)
scrollbar.pack(side=LEFT, fill=Y)

checklist = Text(root, width=20, height= 40,  bg='red')
checklist.place(x = 0, y= 0)


input_area = Canvas(root, width = 145, height= 100, bg= 'black')
input_area.place(x = 0, y= 495)



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

ent = Entry(input_area)
ent.pack()

checklist.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=checklist.yview)

# disable the widget so users can't insert text into it
checklist.configure(state="disabled")

root.mainloop()




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
