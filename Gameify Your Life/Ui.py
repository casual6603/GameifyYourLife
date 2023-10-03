from tkinter import *
from tkinter import ttk
 
 
# Main tkinter window
root = Tk()
root.geometry("960x540")
root.configure(background='gray24')
 
 

 
# right section
right_frame = Frame(root, width=250, height=540, bg='gray15')
right_frame.grid(row=0, column=1)


# left section 
left_frame = Frame(root, width=710, height=540)
left_frame.grid(row=10, column=15)
left_frame.configure(background='gray10')


# text
top_label = Label(right_frame,
                        text ='To do List',
                        background="gray15",
                        fg= "white",
                        font=("Helvetica",18)
                        )
top_label.place(x=50, y=-4)




mainloop()


