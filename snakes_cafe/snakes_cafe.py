print("""
$ python snakes_cafe.py
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************
""")
appetizers = ['Wings', 'Cookies', 'Spring Rolls']
entrees = ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden']
deserts = ['Ice Cream', 'Cake', 'Pie']
drinks = ['Coffee', 'Tea', 'Unicorn Tears']

print("""Appetizers 
----------""")
for appetizer in appetizers:
    print(appetizer)

print("""Entrees 
-------""")
for entree in entrees:
    print(entree)

print("""Deserts 
-------""")
for desert in deserts:
    print(desert)

print("""Drinks
------""")
for drink in drinks:
    print(drink)

print("""
***********************************
** What would you like to order? **
***********************************
""")
menu = {}

while True:
	item = input("> ")
	if item == 'quit':
		break
	elif item not in menu:
		menu[item] = 0
	menu[item] += 1
	print(f"{menu[item]}orders of {item} have been added to your meal")

'''
while item != "quit":
    item = input("> ")
    print(f"{menu[item]}orders of {item} have been added to your meal")
'''
