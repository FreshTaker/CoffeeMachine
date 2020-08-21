"""This is my take of the a Coffee Machine Kiosk Simulator using OOP methods"""

class CoffeeMachine:
    # Initial amounts:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    def machine_status(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"${self.money} of money")

    def buy_coffee(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        drink_choice = input()
        missing = 0
        if drink_choice == "back":
            pass
        if drink_choice == "1":
        # Espresso
            if self.water < 250:
                missing = "water"
            if self.beans < 16:
                missing = "coffee beans"
            if self.cups < 1:
                missing = "cups"

            if missing != 0:
                print(f"Sorry, not enough {missing}!")
            else:
                self.water += -250
                self.beans += -16
                self.cups += -1
                self.money += 4
                print("I have enough resources, making you a coffee!")
        if drink_choice == "2":
            # latte
            if self.water < 350:
                missing = "water"
            if self.milk < 75:
                missing = "milk"
            if self.beans < 20:
                missing = "coffee beans"
            if self.cups < 1:
                missing = "cups"

            if missing != 0:
                print(f"Sorry, not enough {missing}!")
            else:
                self.water += -350
                self.milk += -75
                self.beans += -20
                self.cups += -1
                self.money += 7
                print("I have enough resources, making you a coffee!")
        if drink_choice == "3":
            # Cappuccino
            if self.water < 200:
                missing = "water"
            if self.milk < 100:
                missing = "milk"
            if self.beans < 12:
                missing = "coffee beans"
            if self.cups < 1:
                missing = "cups"

            if missing != 0:
                print(f"Sorry, not enough {missing}!")
            else:
                self.water += -200
                self.milk += -100
                self.beans += -12
                self.cups += -1
                self.money += 6
                print("I have enough resources, making you a coffee!")

    def fill_coffee(self):
        print("Write how many ml of water do you want to add:")
        water_add = int(input())
        print("Write how many ml of milk do you want to add:")
        milk_add = int(input())
        print("Write how many grams of coffee beans do you want to add:")
        beans_add = int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        cups_add = int(input())

        self.water += water_add
        self.milk += milk_add
        self.beans += beans_add
        self.cups += cups_add

    def take_coffee(self):
        print(f"I gave you ${self.money}")
        self.money = 0

# MAIN SEQUENCE:
the_Machine = CoffeeMachine()
while True:
    print("Write action (buy, fill, take, remaining, exit): ")
    action = input()

    if action == "buy":
        the_Machine.buy_coffee()

    if action == "fill":
        the_Machine.fill_coffee()

    if action == "take":
        the_Machine.take_coffee()

    if action == "remaining":
        the_Machine.machine_status()

    if action == "exit":
        break


