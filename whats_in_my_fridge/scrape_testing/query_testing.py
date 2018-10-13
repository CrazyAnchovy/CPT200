import sqlite3
#import sqlalchemy


count = 0

conn = sqlite3.connect("recipe_db.db")
c = conn.cursor()



word = input('what ingredient would you like to search for?')
word2 = input('what other indredient would you like to include?')

chicken_getter = c.execute("SELECT DISTINCT name, ingredients, directions FROM 'recipe_table' WHERE ingredients LIKE '%{}%' AND ingredients LIKE '%{}%'".format(word, word))

recipes = c.fetchall()

#print(recipes)
print(len(recipes))

for recipe in recipes:
    print('******')
    recipe = " ".join([x for x in recipe])
    print(recipe)
    

print(len(recipes))


