import bs4 as bs
import urllib.request


number = 0

with open ('recipe_link_file.txt') as link_file:
    recipe_links = link_file.read().split(',')

link_list = [] 

for link in recipe_links:
    link_list.append(link)
    
    
# for link in link_list:
#     print(link)
    

                                                #this link_list[0] is where i decide to have just one url to practice on
link_source = urllib.request.urlopen(link_list[0]).read()
link_soup = bs.BeautifulSoup(link_source, 'lxml')

pretty_soup = link_soup.prettify()
#print(pretty_soup)

print(link_list[0])




#just getting a file that doesn't get cut off on the top...    
# with open('example_page.txt', 'w') as example_page:
#     for line in pretty_soup:
#         try:
#             example_page.write(line)
#         except:
#             pass

        
        
possible_list = link_soup.find_all('ul', class_ = 'ingredient-list')
print(possible_list)
print('****')

recipe_title = link_soup.find('h1')

print(recipe_title.text)

for item in possible_list:
    print(item.text)
    
recipe_directions = link_soup.find('h4', class_ = 'expanded')
print(recipe_directions)



    





    
    