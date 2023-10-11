import tkinter as tk
from tkinter import *



class ListFrame (tk.Frame):
    def __init__(self, parent, text_data, item_height):
        super().__init__(parent)
        self.pack(expand=True, fill=BOTH)
        
        
        self.text_data = text_data
        self.item_number = len(text_data)
        self.list_height = self.item_number * item_height
        
window = tk.Tk()
window.geometry(500,600)
window.title("scrolling")



text_list = [('item 1', 'item 2', 'item 3', 'item 4'), ('item 5', 'item 6', 'item 7', 'item 8'),('item 9', 'item 10', 'item 11', 'item 12')]
list_frame = ListFrame(window, text_list, 20)

window.mainloop()