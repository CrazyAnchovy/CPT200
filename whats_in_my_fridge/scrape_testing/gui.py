
import tkinter
from tkinter import *



class gui(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.geometry("700x500")
        self.master.title('What\'s in my Fridge?')
        self.grid()
        
        self.enter_button = Button(self, text='Get Recipes!')
        self.enter_button.grid(row=0, column=0)
        
        

gui().mainloop()