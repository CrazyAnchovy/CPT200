import sqlite3
#import sqlalchemy


count = 0

conn = sqlite3.connect("recipe_db.db")
c = conn.cursor()

chicken_getter = c.execute("SELECT * FROM 'recipe_table' WHERE 'ingredients' like '%chicken%' ")

list = c.fetchall()

for item in list:
    print(list[item])
    
print(type(chicken_getter))

print(chicken_getter)


