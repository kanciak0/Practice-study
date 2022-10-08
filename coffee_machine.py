MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
quarter = float(0.25)
dime = float(0.1)
nickel = float(0.05)
penny = float(0.01)


#  TODO: 1. Print the report of all the coffe machines
def coffee_machine():
    finished = False
    while not finished:
        sum = 0
        user_choice = str(input(
            "What would you like? (espresso/latte/cappuccino, if you want to check the resources type:'report', type 'off' to exit loop"))
        if user_choice == "espresso":
            print("Please insert:", MENU['espresso']['cost'], "$")
            # REMEMBER ONLY ESPRESSO WORKS CUZ IM A LAZY FUCK XDDD
            quarter_count = float(input("How many quarters do you have?"))
            sum += quarter_count * quarter

            dime_count = float(input("How many dimes do you have?"))
            sum += dime_count * dime

            nickel_count = float(input("How many nickels do you have?"))
            sum += nickel_count * nickel

            penny_count = float(input("How many pennies do you have?"))
            sum += penny_count * penny

            user_money = sum - MENU['espresso']['cost']
            if user_money > 0:
                print(f"Here is your coffee and your exchange is {user_money}")
                resources["water"] -= 50
                resources["coffee"] -= 18
                print(resources["water"])
                print(resources["coffee"])
                continue
            elif user_money < 0:
                print("You need to insert more money, sorry i cant make a coffe")
        #        elif user_choice == "latte":
        #
        #        elif user_choice == "cappuccino":
        if user_choice == "report":
            for element in resources:
                print(element, resources[element])
                continue
        if user_choice == "off":
            finished = True


coffee_machine()
