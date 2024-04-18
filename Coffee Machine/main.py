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
    "water": 100,
    "milk": 200,
    "coffee": 100,
}


def checkrun(drink):
    """call to check and subtract resources"""
    if drink == 'espresso':
        checkers = ['water', 'coffee']
    elif 'latte' or 'cappuccino':
        checkers = ['water', 'milk', 'coffee']
    for i in checkers:
        levels = resource_check(drink, i)
        if not levels:
             return False
        else:
            remresource(drink, i)
    return True


def resource_check(drink, resource):
    """Check resource"""
    if resources[resource] - MENU[drink]['ingredients'][resource] >= 0:
        # print(f'{resource} works')
        return True
    else:
        print(f'Sorry there is not enough {resource}')
        return False


def remresource(drink, resource):
    resources[resource] = resources[resource] - MENU[drink]['ingredients'][resource]


def payments(drink, money):
    dr_cost = MENU[drink]['cost']
    print(f'Your drink costs ${round(dr_cost,2)}\n')
    if dr_cost == money:
        print(f'Here is your {drink}. Enjoy!')
        return money
    elif dr_cost > money:
        print(f'Sorry that is not enough money. Money refunded.')
        return 0

    else:
        refund = round(money - dr_cost,2)
        print(f'Here is ${refund} in change. Enjoy your {drink}.')
        return money - refund


def coffee_machine():
    profit = 0
    machine_on = True
    materials = True
    while machine_on:
        drink_choices = ['espresso', 'latte', 'cappuccino']
        userchoice = input('\n\nWhat would you like? (espresso/latte/cappuccino)\n').lower()

        if userchoice in drink_choices:
            materials = checkrun(userchoice)

            if materials:
                print('Insert Coins')
                quarters = int(input('How many quarters?\n'))
                dimes = int(input('\nHow many dimes?\n'))
                nickles = int(input('\nHow many nickles?\n'))
                pennies = int(input('\nHow many pennies?\n'))

                total_money = round(0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies, 2)
                print(f'You paid ${total_money}')
                profit += payments(userchoice, total_money)

        elif userchoice == 'report':
            print(f'''
            Water: {resources['water']}
            Milk: {resources['milk']}
            Coffee: {resources['coffee']}
            Money: {profit}
            ''')
        elif userchoice == 'off':
            print('Shutting Down')
            machine_on = False
        else:
            print('ERROR')


coffee_machine()

