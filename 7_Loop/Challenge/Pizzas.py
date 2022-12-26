'''
Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
• Modify your for loop to print a sentence using the name of the pizzainstead of printing just the name of the pizza. For each pizza you should have one line of output containing a simple statement like I like pepperoni pizza.
• Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
'''

pizzas = ['Chicken pizza', 'Ram Pizza', 'Beaf Pizza',]
for pizza in pizzas:
    print(pizza)

# • Modify your for loop to print a sentence using the name of the pizzainstead of printing just the name of the pizza. For each pizza you should have one line of output containing a simple statement like I like pepperoni pizza.
chickenPizza = f"My favourte pizza is {pizzas[0]}"
print(chickenPizza)
ramPizza = f"My favourte pizza is {pizzas[1]}"
print(ramPizza)
beafPizza = f"My favourte pizza is {pizzas[2]}"
print(beafPizza)
