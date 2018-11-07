import sqlite3
import tkinter
from tkinter import *

conn = sqlite3.connect("recipe_db.db")
c = conn.cursor()

class gui(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.geometry("500x400")
        self.master.title('What\'s in my Fridge?')
        self.grid()
        
        self.enter_button = Button(self, text='Get Recipes!', command = self.get_recipes)
        self.enter_button.grid(row=0, column=2)
        
        self.ingredient1_entry = Entry(self)
        self.ingredient1_entry.grid(row=0, column=1)
        
        self.label = Label(self, text='What Ingredient?')
        self.label.grid(row = 0, column = 0)
        
        self.information=Listbox(self, height=20, width=75)
        self.information.grid(row=1, column=0, columnspan=3)
        
    def get_recipes(self):
        ingredient = self.ingredient1_entry.get()
        recipes = c.execute("SELECT DISTINCT name, ingredients, directions FROM 'recipe_table' WHERE ingredients LIKE '%{}%'".format(ingredient))
        
        
         
        for recipe in recipes:
            self.information.insert('end', "****")
            recipe = " ".join([x for x in recipe])
            self.information.insert('end', recipe)

gui().mainloop()