import main


def produce_report():
    print(f"'Water': {main.resources['water']}ml")
    print(f"'Milk': {main.resources['milk']}ml")
    print(f"'Coffee': {main.resources['coffee']}g")
    print(f"'Money': ${main.resources['cost']}")


def check_ingredients(choice):
    present = main.resources
    required = main.MENU[choice]["ingredients"]
    enough = True
    for ingredient in required:
        if present[ingredient] < required[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            enough = False
            break
    if enough:
        for ingredient in required:
            main.resources[ingredient] -= required[ingredient]
    return enough


def check_money(choice, paid):
    enough = True
    if paid < main.MENU[choice]["cost"]:
        enough = False
    else:
        main.resources["cost"] += paid
    return enough


main.resources["cost"] = 0.0
while True:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee_choice == "report":
        produce_report()
        continue
    elif coffee_choice == "off":
        break
    else:
        if coffee_choice not in main.MENU:
            continue
    coffee_status = check_ingredients(coffee_choice)
    if not coffee_status:
        break
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total_paid = round(0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies, 2)
    coffee_status = check_money(coffee_choice, total_paid)
    if not coffee_status:
        print("Sorry that's not enough money. Money refunded.")
        continue
    change = total_paid - main.MENU[coffee_choice]["cost"]
    print(f"Here is your {coffee_choice}☕. Enjoy!")
    print(f"Here is ${change} in change.")

