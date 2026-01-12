from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# Prompting user to tell their order
menu = Menu()
cm = CoffeeMaker()
mm = MoneyMachine()

while True:
    order = input(f"What would you like,{menu.get_items()} : ")
    if order  == 'off':
        break
    if order  == 'report':
        cm.report()
        continue
    if order == 'profit':
        mm.report()
        continue

    print(f"The user has ordered {order}")
    drink = menu.find_drink(order)

    
    # resources sufficient
    if cm.is_resource_sufficient(drink) and mm.make_payment(drink.cost):
        cm.make_coffee(drink)
    else:
        print(f"Sorry, {drink.name}, can't do it.")
