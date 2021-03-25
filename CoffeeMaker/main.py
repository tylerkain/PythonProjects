from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True
# prompt user
while is_on:
    user_drink_choice = input(f" What would you like to drink : {menu.get_items()}: ")
# turn machine off
    if user_drink_choice == "OFF":
        is_on: False
    elif user_drink_choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(user_drink_choice)
        check_resources = coffee_maker.is_resource_sufficient(drink)
        payment = money_machine.make_payment(drink.cost)
        if check_resources and payment:
            coffee_maker.make_coffee(drink)

# print a report




# Process Coins

