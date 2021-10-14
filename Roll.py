from Lib.Dice import *
from Lib.Player import *
from Lib.Store import Store

player = Player()
store = Store(player)

while player.noRolls>0:
    userInput = ""
    while userInput == "":
        try:
            userInput= int(input("What would you like to do? \n 0 - Roll your dice\n 1 - View the store \n> "))
        except:
            print("Error - Invalid number")
    
    if userInput == 0:
        player.roll()
    elif userInput ==1:
        store.viewStore(player)