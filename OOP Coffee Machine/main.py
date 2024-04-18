from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# define all drinks
espresso = MenuItem('espresso', 50, 0, 18, 1.5)
latte = MenuItem('latte', 200, 150, 24, 2.5)
cappuccino = MenuItem('cappuccino', 250, 100, 24, 3)

# create my menu
my_menu = Menu()
# define a coffee machine
coffees = CoffeeMaker()
# start the money machine
moneybags = MoneyMachine()


is_on = True

while is_on:
    name = input(f'What drink would you like? {my_menu.get_items()}\n')

    drink_chosen = my_menu.find_drink(name)

    if drink_chosen != None:
        # connect chosen drink with object
        if name == 'espresso':
            drink_chosen = espresso
        elif name == 'latte':
            drink_chosen = latte
        else:
            drink_chosen = cappuccino

        # check if there are enough resources for the drink
        resource_check = coffees.is_resource_sufficient(drink_chosen)
        if resource_check:
            process = moneybags.make_payment(drink_chosen.cost)
            if coffees.make_coffee(drink_chosen):
                coffees.make_coffee(drink_chosen)


    elif name == 'report':
        coffees.report()
        moneybags.report()
    else:
        print('Shutting down')
        is_on = False

