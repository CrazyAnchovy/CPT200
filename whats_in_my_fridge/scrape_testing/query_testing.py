import sqlite3
#import sqlalchemy

string = """

8  lamb chops or 8    skinless chicken pieces, on bone but skin & fat free if possible
1  large  onion
3  garlic cloves
2  medium  carrots
2  medium  courgettes (zucchini)
2  large  potatoes
1⁄4 swede or 1⁄4 turnip
1  parsnip
2 -3  stalks  celery (or khorchef)
1  cup  chickpeas, drained
2  teaspoons  ras el hanout spice mix
  salt & pepper
1  pinch  dried mint
1⁄2 tablespoon  sunflower oil or 1⁄2 tablespoon  vegetable oil
1  cup of tinned plum tomato, liquidised
1 1⁄2 liters  water
1  large  green chili pepper (the Algerian ones) (optional)
500  g medium couscous
1  tablespoon  ghee (smen)
1 1⁄2 tablespoons  margarine
1  glass  water
 olive oil

"""
count = 0

conn = sqlite3.connect("recipe_db.db")
c = conn.cursor()

word = 'chicken'

chicken_getter = c.execute("SELECT name FROM 'recipe_table' WHERE ingredients LIKE '%{}%'".format(word))

recipes = c.fetchall()

#print(recipes)
print(len(recipes))
for recipe in recipes:
    recipe = " ".join([x for x in recipe])
    print(recipe)
    




