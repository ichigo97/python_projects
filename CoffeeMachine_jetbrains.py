
class coffee_machine():
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coff_beans = 120
        self.disp_cups = 9
        self.money = 550
        
        while True:
            choice = input("Write action (buy, fill, take, remaining, exit):")
            temp = self.get_input(choice)
            if temp == "exit":
                break
        
    def get_input(self,action):
        a = self.process(action)
        return a
            
    def process(self,action):
        
        global water, milk, coff_beans, money, disp_cups, in_state 
        self.in_state = "Choosing an action"
        if self.in_state == "Choosing an action":
            if action == "buy":
                self.in_state = "choosing a type of coffee"
                self.order = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:, back - to main menu:")
                self.in_state = "choosing a type of coffee"
                if min((self.water - 250), (self.water - 350), (self.water - 200)) < 0:
                    print("Sorry, not enough water")
                elif min((self.coff_beans - 16), (self.coff_beans - 20), (self.coff_beans - 12)) < 0:
                    print("Sorry, not enough coffee beans")
                elif min((self.milk - 75), (self.milk - 100)) < 0:
                    print("Sorry, not enough milk")
                elif (self.disp_cups - 1) < 0:
                    print("Sorry, not enough disposable cups")
                else:
                    print("I have enough resources, making you a coffee!")
                    if self.order == "1":
                        self.water -= 250
                        self.coff_beans -= 16
                        self.disp_cups -= 1
                        self.money += 4
                    elif self.order == "2":
                        self.water -= 350
                        self.milk -= 75
                        self.coff_beans -= 20
                        self.disp_cups -= 1
                        self.money += 7
                    elif self.order == "3":
                        self.water -= 200
                        self.milk -= 100
                        self.coff_beans -= 12
                        self.disp_cups -= 1
                        self.money += 6
                    elif self.order == "back":
                        pass
                self.in_state = "Choosing an action"
                
            elif action == "fill":
                self.water += int(input("Write how many ml of water do you want to add:"))
                self.milk += int(input("Write how many ml of self.milk  do you want to add:"))
                self.coff_beans += int(input("Write how many grams of coffee beans do you want to add:"))
                self.disp_cups += int(input("Write how many disposable cups of coffee do you want to add:"))
                
            elif action == "take" :        
                print("I gave you $", self.money)
                self.money = 0
            elif action == "remaining":
                print("The coffee machine has:")
                print(self.water, " of water")
                print(self.milk, " of self.milk")
                print(self.coff_beans, " of coffee beans")
                print(self.disp_cups, " of disposable cups")
                print(self.money, " of self.money")
            elif action == "exit":
                return "exit"
coffee_machine()
