import sqlite3
#import sqlalchemy


count = 0

conn = sqlite3.connect("recipe_db.db")
c = conn.cursor()


print('input NONE to end query')

ingredient_list = []
ingredient = ''

while ingredient != 'NONE':
    ingredient = input('what ingredient would you like to search for?')
    ingredient_list.append(ingredient)
    
c.execute("SELECT DISTINCT name, ingredients, directions FROM 'recipe_table' WHERE ingredients LIKE '%{}%' AND ingredients LIKE '%{}%'".format(ingredient, ingredient))

recipes = c.fetchall()

#print(recipes)
print(len(recipes))

for recipe in recipes:
    print('******')
    recipe = " ".join([x for x in recipe])
    print(recipe)
    

print(len(recipes))


