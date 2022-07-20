from days.day_016.files.helpers import *
from days.day_016.files.money_machine import MoneyMachine
from days.day_016.files.menu import Menu
from days.day_016.files.coffee_maker import CoffeeMaker


def day_016():
	title("OOP COFFEE MACHINE")
	money_machine = MoneyMachine()
	coffee_maker = CoffeeMaker()
	menu = Menu()
	is_on = True

	while is_on:
		options = menu.get_items()
		choice = nli(f"What would you like?\n{options}\n")
		if choice == "off":
			is_on = False
		elif choice == "report":
			coffee_maker.report()
			money_machine.report()
		else:
			selectable = menu.menu_choices()
			while choice not in selectable:
				cls()
				nls("Sorry, that item is not available.")
				choice = nli(f"What would you like?\n{options}\n")
			drink = menu.find_drink(choice)

			if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
				coffee_maker.make_coffee(drink)
				again = nli("Would you like more coffee?\n'y' or 'n'")
				if again == 'n':
					cls()
					is_on = False
				else:
					cls()
					if not coffee_maker.is_resource_sufficient(drink):
						is_on = False