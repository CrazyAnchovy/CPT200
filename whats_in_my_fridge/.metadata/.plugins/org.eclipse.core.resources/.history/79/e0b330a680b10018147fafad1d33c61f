import bs4 as bs
import urllib.request

#namespace
link_list = []

#define classes
class Recipe:
    """Recipe is an object which has a name, directions and ingredients"""
    def __init__(self, name, directions, ingredients):
        self.name = name
        self.directions = directions
        self.ingredients = ingredients
    pass

class Refrigerator:
    pass



with open ('recipe_link_file.txt') as link_file:
    recipe_links = link_file.read().split(',')
    
for link in recipe_links:
    link_list.append(link)
    
    