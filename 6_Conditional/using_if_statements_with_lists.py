'''
check whether the list of requested toppings is empty before building the pizza. If the list is empty, we’ll prompt the user and make sure they want a plain pizza. If the list is not empty, we’ll build the pizza just as we did in the previous examples
'''

requested_toppings = []  # In this example, we already Know that the list is Empty, but we just want to Check if the requested pizza is there, that's why we use the if statement to chech

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain Pizza")
'''
This time we start out with an empty list of requested toppings at u. Instead of jumping right into a for loop, we do a quick check at v. When the name of a list is used in an if statement, Python returns True if the list contains at least one item; an empty list evaluates to False. If requested_toppings passes the conditional test, we run the same for loop we used in the previous example. If the conditional test fails, we print a message asking the customer if they really want a plain pizza with no toppings w. The list is empty in this case, so the output asks if the user really wants a plain pizza:
'''
