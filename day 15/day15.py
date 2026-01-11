MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    },
}

resources = {"water": 300, "milk": 200, "coffee": 100}

while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "off":
        break

    if user_choice == "report":
        print(resources)
        continue

    if user_choice not in MENU:
        print("Invalid choice.")
        continue

    # Check resources
    for item, amount in MENU[user_choice]["ingredients"].items():
        if resources[item] < amount:
            print(f"Sorry, not enough {item}.")
            break
    else:
        # Take money
        quarters = int(input("How many quarters: "))
        dimes = int(input("How many dimes: "))
        nickles = int(input("How many nickles: "))
        pennies = int(input("How many pennies: "))

        total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
        cost = MENU[user_choice]["cost"]

        if total < cost:
            print("Sorry, not enough money. Refunded.")
            continue

        # Deduct resources
        for item, amount in MENU[user_choice]["ingredients"].items():
            resources[item] -= amount

        change = total - cost
        if change > 0:
            print(f"Here is your change: ${change:.2f}")

        print(f"Here is your {user_choice}. Enjoy!")
