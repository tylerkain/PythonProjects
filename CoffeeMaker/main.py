from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu= Menu()
menu.get_items()

# prompt user

user_drink_choice = input(f" What would you like to drink : {menu.get_items()}: ")
drink = menu.find_drink(user_drink_choice)

# turn machine off
if user_drink_choice == "off":
    print("CoffeeMachine is off")

# print a report
coffee_maker = CoffeeMaker()
if user_drink_choice == "report":
    print(coffee_maker.report())

# Check Resources sufficient

 if coffee_maker.is_resource_sufficient(drink):
     coffee_maker.make_coffee(drink)