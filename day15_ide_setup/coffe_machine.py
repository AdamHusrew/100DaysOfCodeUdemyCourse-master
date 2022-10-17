from flavours import MENU

balance = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def has_enough_resource(resource):
    for item in resource:
        if resource[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def proces_payment():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_payment_succesfull(payment, cost):
    if payment >= cost:
        change = round(payment - cost, 2)
        print(f"Here is ${change} in change")
        global balance
        balance += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(request, drink):
    for item in drink:
        resources[item] -= drink[item]
    print(f"Here is your {request} ☕️. Enjoy!")


def print_menu():
    for item in MENU:
        print(f"Item name: {item}\t\tItem cost: {MENU[item]['cost']}")


def run():
    turn_on = True
    while turn_on:
        request = input("What would you like? (menu/espresso/latte/cappuccino/report/off): ").lower()

        if request == "off":
            turn_on = False
        elif request == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${balance}")
        elif request == "menu":
            print_menu()
        else:
            drink = MENU[request]
            if has_enough_resource(drink["ingredients"]):
                payment = proces_payment()
                if is_payment_succesfull(payment, drink["cost"]):
                    make_coffee(request, drink["ingredients"])


run()
