# Write your code here
import sys

ESPRESSO = [250, 0, 16, 4]
LATTE = [350, 75, 20, 7]
CAPPUCCINO = [200, 100, 12, 6]


class Coffee:
    all_water = 400
    all_milk = 540
    all_beans = 120
    all_cups = 9
    all_money = 550


def coffee_machine_has():
    print('The coffee machine has:')
    print(Coffee.all_water, "of water")
    print(Coffee.all_milk, "of milk")
    print(Coffee.all_beans, "coffee of beans")
    print(Coffee.all_cups, "of disposable cups")
    print("$" + str(Coffee.all_money), "of money")
    print("")


def take_money():
    print("I gave you $" + str(Coffee.all_money))
    Coffee.all_money = 0
    print("")


def fill():
    print("Write how many ml of water do you want to add:")
    fill_water = int(input())
    Coffee.all_water += fill_water
    print("Write how many ml of milk do you want to add:")
    fill_milk = int(input())
    Coffee.all_milk += fill_milk
    print("Write how many grams of coffee beans do you want to add:")
    fill_beans = int(input())
    Coffee.all_beans += fill_beans
    print("Write how many disposable cups of coffee do you want to add:")
    fill_cups = int(input())
    Coffee.all_cups += fill_cups
    print("")


def what_coffee_we_can(coffee):
    if coffee[0] <= Coffee.all_water and coffee[1] <= Coffee.all_milk and coffee[2] <= Coffee.all_beans and Coffee.all_cups >= 1:
        print("I have enough resources, making you a coffee!")
        make_coffee(coffee)
    elif coffee[0] > Coffee.all_water:
        print("Sorry, not enough water!")
    elif coffee[1] > Coffee:
        print("Sorry, not enough milk!")
    elif coffee[2] > Coffee:
        print("Sorry, not enough beans!")
    else:
        print("Sorry, not enough cups!")
    print("")


def make_coffee(coffee):
    Coffee.all_water -= coffee[0]
    Coffee.all_milk -= coffee[1]
    Coffee.all_beans -= coffee[2]
    Coffee.all_money += coffee[3]
    Coffee.all_cups -= 1


def buy_coffee(number):
    if number == "1":
        what_coffee_we_can(ESPRESSO)
    elif number == "2":
        what_coffee_we_can(LATTE)
    else:
        what_coffee_we_can(CAPPUCCINO)


def action_coffee(my_action):
    if my_action == "fill":
        fill()
    elif my_action == "buy":
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        number = input()
        if number == "back":
            main()
        else:
            buy_coffee(number)
    elif my_action == "remaining":
        coffee_machine_has()
    else:
        take_money()
    main()


def main():
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    print("")
    if action == "exit":
        sys.exit(0)
    else:
        action_coffee(action)


main()
