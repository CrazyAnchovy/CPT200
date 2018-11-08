import sqlite3
import tkinter
from tkinter import *

conn = sqlite3.connect("recipe_db.db")
c = conn.cursor()
ingredients_list = []

class gui(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.geometry("700x400")
        self.master.title('What\'s in my Fridge?')
        self.grid()
        
        self.enter_button = Button(self, text='Get Recipes!', command = self.get_recipes)
        self.enter_button.grid(row=0, column=2)
        
        self.ingredient1_entry = Entry(self)
        self.ingredient1_entry.grid(row=0, column=1)
        
        self.ingredient2_entry = Entry(self)
        self.ingredient2_entry.grid(row=1, column=1)
        
        self.ingredient3_entry = Entry(self)
        self.ingredient3_entry.grid(row=2, column=1)

        self.ingredient4_entry = Entry(self)
        self.ingredient4_entry.grid(row=3, column=1)

        self.ingredient5_entry = Entry(self)
        self.ingredient5_entry.grid(row=4, column=1)


        
        self.label = Label(self, text='What Ingredient?')
        self.label.grid(row = 0, column = 0)
        
        self.information=Listbox(self, height=20, width=50)
        self.information.grid(row=0, column=4, columnspan=1, rowspan=5)
        
    def get_recipes(self):
        ingredient_counter = 0
        ingredient1 = self.ingredient1_entry.get()
        ingredient2 = self.ingredient2_entry.get()
        ingredient3 = self.ingredient3_entry.get()
        ingredient4 = self.ingredient3_entry.get()
        ingredient5 = self.ingredient3_entry.get()
        
        ingredients_list.append(ingredient1)
        ingredients_list.append(ingredient2)
        ingredients_list.append(ingredient3)
        ingredients_list.append(ingredient4)
        ingredients_list.append(ingredient5)
        
        for ingredient in ingredients_list:
            if ingredient != '':
                ingredient_counter += 1
                            
        if ingredient_counter == 1:
            recipes = c.execute("SELECT DISTINCT name, ingredients, directions FROM 'recipe_table' WHERE ingredients LIKE '%{}%'".format(ingredient1))
        elif ingredient_counter == 2:
            recipes = c.execute("SELECT DISTINCT name, ingredients, directions FROM 'recipe_table' WHERE ingredients LIKE '%{}%' and ingredients LIKE '%{}%'".format(ingredient1, ingredient2))
        elif ingredient_counter == 3:
            recipes = c.execute("SELECT DISTINCT name, ingredients, directions FROM 'recipe_table' WHERE ingredients LIKE '%{}%' and ingredients LIKE '%{}%' and ingredients LIKE '%{}%'".format(ingredient1, ingredient2, ingredient3))
        elif ingredient_counter == 4:
            recipes = c.execute("SELECT DISTINCT name, ingredients, directions FROM 'recipe_table' WHERE ingredients LIKE '%{}%' and ingredients LIKE '%{}%' and ingredients LIKE '%{}%' and ingredients LIKE '%{}%'".format(ingredient1, ingredient2, ingredient3, ingredient4))
        elif ingredient_counter == 5:
            recipes = c.execute("SELECT DISTINCT name, ingredients, directions FROM 'recipe_table' WHERE ingredients LIKE '%{}%' and ingredients LIKE '%{}%' and ingredients LIKE '%{}%' and ingredients LIKE '%{}%' and ingredients LIKE '%{}%'".format(ingredient1, ingredient2, ingredient3, ingredient4, ingredient5))
        
        for recipe in recipes:
            self.information.insert('end', "****")
            recipe = " ".join([x for x in recipe])
            self.information.insert('end', recipe)
        
        
        #the next few lines to be defined as a function for 'reset'    
        ingredient_counter = 0
        recipes = ''
        for ingredient in ingredients_list:
            ingredients_list.pop()
        #self.information.delete(0,END)

        
gui().mainloop()

