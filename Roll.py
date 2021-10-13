from Lib.Dice import *
from Lib.Player import *

player = Player()

while player.noRolls>0:
    userInput = ""
    while userInput == "":
        try:
            userInput= int(input("What would you like to do? \n 0 - Roll your dice \n> "))
        except:
            print("Error - Invalid number")
    
    if userInput == 0:
        player.roll()