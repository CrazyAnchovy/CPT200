import sqlite3
#import sqlalchemy




conn = sqlite3.connect("1-recipe_db.db")
c = conn.cursor()

chicken_getter = c.execute("SELECT * FROM 'recipe_table' WHERE 'ingredients' like 'ingredient_string' ")

for item in chicken_getter:
    print(chicken_getter.fetchall())