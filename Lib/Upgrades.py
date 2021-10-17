from random import randint

from Lib.Face import *

class Upgrade:
    cost = 0
    quantity = 1
    face= None
    # this is directly tied in with the level of the store. 
    # As levels go up, items become more expensive but also more powerful
    level = 1
    def __init__(self, cost, level,refreshes) -> None:
        self.cost = cost*refreshes**level
        self.level = level

    # This is used for upgrades that overwrite the value of other die faces
    def replaceFace(self, dice):
        i = 0
        for x in dice:
            print("Dice #" +str(i))
            print(x)
        
        while True:
            try:
                playerInput = input("which die and face would you like to replace? e.g 1,3 means first die, 3rd face\n> ")

                playerInput=playerInput.split(",")

                chosenDice = dice[int(playerInput[0])]
                chosenDice.setFace(int(playerInput[1])-1,self.face)
                return

            except:
                print("error invalid die or face")

    def __str__(self):
        return(self.name +"\nCost: $" +str(self.cost) +"\nQuantity in stock: " + str(self.quantity) +"\n")

# This will completely replace another number
# e.g if this has a value of 5 and you place it on a 
# face with a value of 1, the new value of the face
# is 5
class NumberReplaceUpgrade(Upgrade):

    def __init__(self, cost, level, refreshes) -> None:
        super().__init__(cost,level,refreshes)
        self.number = min(randint(1,max(10*level,1)),99)
        self.name = "Number Replace: " + str(self.number)
        self.face = NumberFace(self.number)
    def buy(self, player):
        self.replaceFace(player.dice)
        self.quantity = 0
        player.money -= self.cost

    

    

    