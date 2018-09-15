import sqlite3

conn = sqlite3.connect("practice_db.db")

c = conn.cursor()

# c.execute("""CREATE TABLE practice(
#             name text,
#             ingredients text,
#             directions text
#         )""")

#c.execute("INSERT INTO practice VALUES ('food', 'ingredients', 'make it')")

c.execute("SELECT * FROM practice WHERE name = 'food'")
selection = c.fetchall()
print(selection)

conn.commit()

conn.close()