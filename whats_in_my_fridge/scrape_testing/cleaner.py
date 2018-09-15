import bs4 as bs
import urllib.request

#namespace
url_number = 0
link_list = []
string_ingredients = []
string_directions = []
ingredient_string = ""
directions_string = ""

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
    link_source = urllib.request.urlopen(link_list[url_number]).read()
    link_soup = bs.BeautifulSoup(link_source, 'lxml')
    
    recipe_title = link_soup.find('h1')
    print(recipe_title.text)
    #
    
    ingredient_list = link_soup.find_all('ul', class_ = 'ingredient-list')
    for item in ingredient_list:
        print(item.text)
        string_ingredients.append(str(item.text))
        #make this list into one string object
    ingredient_string = ''.join(string_ingredients)
    
    recipe_directions_soup = link_soup.find('div', class_ = 'directions-inner container-xs')
    for item in recipe_directions_soup.find_all('li'):
        if "Submit a Correction" in item.get_text():
            continue
        string_directions.append(str(item.text))
        #make this list into one string object
        print(item.get_text())
    directions_string = ''.join(string_directions)
    
    url_number+=1
    
