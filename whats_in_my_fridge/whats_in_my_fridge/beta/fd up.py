#sponsored recipe selection (skip the first several, to not appear to have dupes)
#work on clickable-ness  (highlightable-ness)
#scrollbars
#add reset to sponsor listboxssssssssszx

import sqlite3
import tkinter as tk
from tkinter import *
import tkinter as ttk
from _operator import mul

conn = sqlite3.connect("recipe_db.db")
c = conn.cursor()
ingredients_list = []

class gui(Frame):
    
    class recipe():
        def __init__(self):
            name = recipe.name
            ingredients = recipe.ingredients
            directions = recipe.directions
    
            
    def __init__(self):
        """initiate the UI"""
        Frame.__init__(self)
        self.master.geometry("875x475")
        
        photo=PhotoImage(file="programbackground.gif")
        label = Label(self,image = photo)
        label.image = photo
        label.grid(row=0,column=0,columnspan=100,rowspan=100)

        self.master.title('What\'s in my Fridge?')
        
        self.grid()
        
        self.label_fake = Label(self, bg="White", fg="Black" , text='Sponsored Recipes:')
        self.label_fake.grid(row = 9, column = 1)
        
        self.label = Label(self, bg="white", fg="black", text='Ingredients on Hand:')
        
        self.label.grid(row = 0, column = 1)
        
        self.enter_button = Button(self, text='Get Recipes!',bg="white", fg="black", command = self.get_recipes)
        self.enter_button.grid(row=6, column=1)
        
        self.reset_button = Button(self, text='Reset',bg="white", fg="Red", command = self.reset)
        self.reset_button.grid(row=7, column=1)
        
        self.recipe_card_button = Button(self, text='Open Recipe', bg="white", fg="black", command = self.open_file_from_listbox)
        self.recipe_card_button.grid(row=7, column=2)
        
        self.ingredient1_entry = Entry(self,bg="Grey", fg="white")
        self.ingredient1_entry.grid(row=1, column=1)
        
        self.ingredient2_entry = Entry(self,bg="Grey", fg="white")
        self.ingredient2_entry.grid(row=2, column=1)
        
        self.ingredient3_entry = Entry(self,bg="Grey", fg="white")
        self.ingredient3_entry.grid(row=3, column=1)

        self.ingredient4_entry = Entry(self,bg="Grey", fg="white")
        self.ingredient4_entry.grid(row=4, column=1)

        self.ingredient5_entry = Entry(self,bg="Grey", fg="white")
        self.ingredient5_entry.grid(row=5, column=1)
        
        self.information=Listbox(self, selectmode = EXTENDED, height=20, width=75)
        self.information.grid(row=1, column=5, columnspan=1, rowspan=5)

        self.Sponsors=Listbox(self, selectmode = EXTENDED, height=5, width=75)
        self.Sponsors.grid(row=7, column=3, columnspan=7, rowspan=3)

    def get_recipes(self):
        recipe_counter = 0
        recipes = ()
        the_recipe = []
        
        self.information.delete(0, 'end')
        for ingredient in ingredients_list:
            ingredients_list.pop()
            
        
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
            #make recipe counter to include a minor amount of recipes in the 'sponsored' recipes (use mod)
            name = recipe[0]
            ingredients = recipe[1]
            directions = recipe[2]
            

            
#             the_recipe.append(str(name))   
#             the_recipe.append(str(ingredients))  
#             the_recipe.append(str(directions))
#             
#             recipe_string = ''.join(the_recipe) 

            self.information.insert('end', name)
            self.information.insert('end', ingredients,)
            self.information.insert('end', directions,)

            self.information.insert('end', "--------------------------------------------------------------------------------------------------")
            recipe_counter += 1
            
            if recipe_counter%10 == 0:
                self.Sponsors.insert('end', name)
                
                
        self.ingredient_counter = 0
        self.recipes = ''
        for ingredient in ingredients_list:
            ingredients_list.pop()

    def reset(self):
        self.ingredient_counter = 0
        self.recipes = ''
        for ingredient in ingredients_list:
            ingredients_list.pop()
        self.information.delete(0,END)
        self.Sponsors.delete(0, END)
        self.ingredient1_entry.delete(0, END)
        self.ingredient2_entry.delete(0, END)
        self.ingredient3_entry.delete(0, END)
        self.ingredient4_entry.delete(0, END)
        self.ingredient5_entry.delete(0, END)
    
    def open_file_from_listbox(self):
        #this function will open highlighted recipe text into a printable txt file
        recipes = [self.information.get(idx) for idx in self.information.curselection()]
        with open('recipe_file.txt', 'w') as recipe_file:
            for entry in recipes:
                recipe_file.write(entry)
        open('recipe_file.txt')
                
        
        
        #recipe_card = self.information.get(ANCHOR)
        
    
      
gui().mainloop()

