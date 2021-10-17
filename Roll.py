from Lib.Dice import *
from Lib.Player import *
from Lib.Store import Store

player = Player()
store = Store()

while player.noRolls>0:
    userInput = ""
    while userInput == "":
        try:
            userInput= input("\nWhat would you like to do? \n> roll\n> roll [x] (roll x times)\n> roll until [x] (roll until you have $x)\n> shop\n> ")
        
            # Roll commands
            if "roll" in userInput:
                userInput = userInput.split(" ")

                # Roll untill you have a certain amount of money
                if "until" in userInput:
                    player.rollUntil(userInput[-1])

                # Roll X Times
                elif userInput[-1].isdigit():
                    player.rollX(userInput[-1])

                # Roll once
                else:
                    player.roll()

            # Go to shop
            elif userInput == "shop":
                store.viewStore(player)

        except:
            print("Error - Invalid command")