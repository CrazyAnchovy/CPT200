import sqlite3
import tkinter as tk
from tkinter import *
import tkinter as ttk
from _operator import mul
import os
import webbrowser


conn = sqlite3.connect("recipe_db.db")
c = conn.cursor()
ingredients_list = []
url = "https://github.com/CrazyAnchovy/CPT200/blob/master/README.md"

class gui(Frame):
    """define the class for the gui"""
    class recipe():
        """define recipe class, might not be used"""
        def __init__(self):
            name = recipe.name
            ingredients = recipe.ingredients
            directions = recipe.directions
    
    def __init__(self):
        """initiate the gui class"""
        Frame.__init__(self)
        self.master.geometry("800x550")

        self.master.title('What\'s in my Fridge?')
        
        self.grid() #define what method we are using to organize

        #install the background photo
        # photo=PhotoImage(file="programbackground.gif")
        # label = Label(self,image = photo)
        # label.image = photo
        # label.grid(row=0,column=0,columnspan=100,rowspan=100)
        
        #install labels
        self.label = Label(self, bg="white", fg="black", text='Enter up to five ingredients below')
        self.label.grid(row = 0, column = 1, padx=10, pady=10)
        
        #install buttons
        self.enter_button = Button(self, text='Get Recipes!',bg="white", fg="black", command = self.get_recipes)
        self.enter_button.grid(row=6, column=1, padx=10, pady=10)
             
        self.recipe_card_button = Button(self, text='Open Recipe', bg="white", fg="black", command = self.open_file_from_listbox)
        self.recipe_card_button.grid(row=7, column=1, padx=10, pady=10)

        self.reset_button = Button(self, text='Reset',bg="white", fg="Red", command = self.reset)
        self.reset_button.grid(row=8, column=1, padx=10, pady=10)

        self.mitch_button = Button(self, text='About',bg="white", fg="Red", command = self.learn_about_mitch)
        self.mitch_button.grid(row=9, column = 1)

        
        #install entry fields
        self.ingredient1_entry = Entry(self,bg="Grey", fg="white")
        self.ingredient1_entry.grid(row=1, column=1, padx=10)
        
        self.ingredient2_entry = Entry(self,bg="Grey", fg="white")
        self.ingredient2_entry.grid(row=2, column=1, padx=10)
        
        self.ingredient3_entry = Entry(self,bg="Grey", fg="white")
        self.ingredient3_entry.grid(row=3, column=1, padx=10)

        self.ingredient4_entry = Entry(self,bg="Grey", fg="white")
        self.ingredient4_entry.grid(row=4, column=1, padx=10)

        self.ingredient5_entry = Entry(self,bg="Grey", fg="white")
        self.ingredient5_entry.grid(row=5, column=1, padx=10)
        
        #install listbox fields
        self.information=Listbox(self, selectmode = EXTENDED, height=27, width=75)
        self.information.grid(row=1, column=5, columnspan=1, rowspan=8, padx=10)

    #callback functions
    def get_recipes(self):
        """this function is the callback for the get recipes button. it is the
           database query for what we want"""          
        #first, clear out previous queries   
        recipe_counter = 0
        recipes = ()
        the_recipe = []
        
        self.information.delete(0, 'end')
        for ingredient in ingredients_list:
            ingredients_list.pop()
            
        #gather what is entered in the ingredient entry fields
        ingredient_counter = 0
        ingredient1 = self.ingredient1_entry.get()
        ingredient2 = self.ingredient2_entry.get()
        ingredient3 = self.ingredient3_entry.get()
        ingredient4 = self.ingredient3_entry.get()
        ingredient5 = self.ingredient3_entry.get()
        
        #add ingredients to the query to list
        ingredients_list.append(ingredient1)
        ingredients_list.append(ingredient2)
        ingredients_list.append(ingredient3)
        ingredients_list.append(ingredient4)
        ingredients_list.append(ingredient5)
        
        #count how many ingredients
        for ingredient in ingredients_list:
            if ingredient != '':
                ingredient_counter += 1
        
        #query based on how many ingredients we are using                    
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
        
        #once we have queried, iterate through the query and insert recipes into the information box
        for recipe in recipes:
            name = recipe[0]
            ingredients = recipe[1]
            directions = recipe[2]

            self.information.insert('end', name)
            self.information.insert('end', ingredients)
            self.information.insert('end', directions)

            self.information.insert('end', "--------------------------------------------------------------------------------------------------")
            recipe_counter += 1
         
        #clear out counters and lists to prevent crash if new query is made before reset happens
        self.ingredient_counter = 0
        self.recipes = ''
        for ingredient in ingredients_list:
            ingredients_list.pop()

    def reset(self):
        """clear all entries and listboxes as well as lists and counters"""
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
        # sponsored_recipes = [self.Sponsors.get(idx) for idx in self.Sponsors.curselection()]
        with open('recipe_file.txt', 'w', encoding='utf-8') as recipe_file:
            for entry in recipes:
                recipe_file.write(entry + '\n')
                recipe_file.write('***********************' + '\n')               
            os.startfile('recipe_file.txt')

    def learn_about_mitch(self):
        webbrowser.open(url)
                
gui().mainloop()
#run the gui, which calls all of the features

