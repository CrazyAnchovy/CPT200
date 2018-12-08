import sqlite3

conn = sqlite3.connect("recipe_db.db")
c = conn.cursor()

ingredient_list = []
ingredient = ''


while ingredient != 'NONE':
    ingredient = input('what ingredient would you like to search for?(input NONE to end query)')
    if ingredient != 'NONE':
        ingredient_list.append(ingredient)
    
for ingredient in ingredient_list:
    c.execute("SELECT DISTINCT name, ingredients, directions FROM 'recipe_table' WHERE ingredients LIKE '%{}%'".format(ingredient))