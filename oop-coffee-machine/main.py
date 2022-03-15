from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
cash_counter = MoneyMachine()

machine_off = False
while not machine_off:
    user_input = input(f"What would you like? {menu.get_items()}: ").lower()
    if user_input == "report":
        coffee_machine.report()
        cash_counter.report()
        continue
    elif user_input == "off":
        machine_off = True
        break

    coffee_choice = menu.find_drink(user_input)
    if coffee_choice is None:
        continue
    place_order = True
    place_order = coffee_machine.is_resource_sufficient(coffee_choice)
    if not place_order:
        break
    place_order = cash_counter.make_payment(coffee_choice.cost)
    if place_order:
        coffee_machine.make_coffee(coffee_choice)