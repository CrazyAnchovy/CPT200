import bs4 as bs
import urllib.request

link_list = [] 
ingredients = []

with open ('recipe_link_file.txt') as link_file:
    recipe_links = link_file.read().split(',')

for link in recipe_links:
    link_list.append(link)
    
link_source = urllib.request.urlopen(link_list[12345]).read()

link_soup = bs.BeautifulSoup(link_source, 'lxml')

ingredient_list = link_soup.find_all('ul', class_ = 'ingredient-list')

recipe_title = link_soup.find('h1')

print(recipe_title.text)

for item in ingredient_list:
    print(item.text)
    string_thing = (str(item.text))
    ingredients.append(string_thing)
    
ing_string = (''.join(ingredients))

print("**")

print('this is the ing_string')
print(ing_string)





    

recipe_directions_soup = link_soup.find('div', class_ = 'directions-inner container-xs')

for item in recipe_directions_soup.find_all('li'):
    if "Submit a Correction" in item.get_text():
        continue
    print(item.get_text())