#bbrune5369@msn.com would like a copy of this program when 'finished' Ginger

import bs4 as bs
import urllib.request
import sqlite3
import time
import csv

#namespace
url_number = 0
link_list = []
string_ingredients = []
string_directions = []
ingredient_string = ""
directions_string = ""

#make the sqlite3 db comment out the following after db is created
conn = sqlite3.connect("recipe_db.db")
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS recipe_table(
            name TEXT,
            ingredients TEXT,
            directions TEXT
        )""")

#soup prep, getting the urls
with open ('recipe_link_file.txt') as link_file:
    recipe_links = link_file.read().split(',')
    
for link in recipe_links:
    link_list.append(link)

#define classes
class Refrigerator:
    """Refrigerator will be the current ingredients owned by the end user"""
    pass

class Recipe:
    """Recipe is an object which has a name, directions and ingredients"""
    def __init__(self, name, directions, ingredients):
        self.name = name
        self.directions = directions
        self.ingredients = ingredients

    #create database of recipes
for link in link_list:
    string_ingredients = []
    string_directions = []
    link_source = urllib.request.urlopen(link_list[url_number]).read()
    link_soup = bs.BeautifulSoup(link_source, 'lxml')
    link_soup.prettify()
    
    recipe_title = link_soup.find('h1')
    recipe_title_string = recipe_title.text
    #print(recipe_title_string)
    
    ingredient_list = link_soup.find_all('ul', class_ = 'ingredient-list')
    for item in ingredient_list:
        #print(item.text)
        string_ingredients.append(str(item.text))
        #make this list into one string object
    ingredient_string = ''.join(string_ingredients)
    #print(str(ingredient_string))
    
    recipe_directions_soup = link_soup.find('div', class_ = 'directions-inner container-xs')
    for item in recipe_directions_soup.find_all('li'):
        if "Submit a Correction" in item.get_text():
            continue
        string_directions.append(str(item.text))
        #make this list into one string object
        #print(item.get_text())
    directions_string = ''.join(string_directions)
    #print(str(directions_string))

    #csv_writer.writerow([recipe_title_string, ingredient_string, directions_string])
    #time.sleep(.5)
    url_number+=1
    print(url_number)
    
    
    c.execute("INSERT INTO recipe_table VALUES (?,?,?)", (recipe_title_string, ingredient_string, directions_string))
    conn.commit()
    
conn.commit()
conn.close()
    
