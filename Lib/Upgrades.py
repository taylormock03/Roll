from random import randint

class Upgrade:
    cost = 0
    quantity = 1
    # this is directly tied in with the level of the store. 
    # As levels go up, items become more expensive but also more powerful
    level = 1
    def __init__(self, cost, level,refreshes) -> None:
        self.cost = cost*refreshes**level
        self.level = level

    # This is used for upgrades that overwrite the value of other die faces
    def replaceFace(self, dice):
        pass

    def __str__(self):
        return(self.name +"\nCost: $" +str(self.cost) +"\nQuantity in stock: " + str(self.quantity) +"\n")

# This will completely replace another face
# e.g if this has a value of 5 and you place it on a 
# face with a value of 1, the new value of the face
# is 5
class FaceReplaceUpgrade(Upgrade):

    def __init__(self, cost, level, refreshes) -> None:
        super().__init__(cost,level,refreshes)
        self.number = min(randint(1,max(10*level,1)),99)
        self.name = "Face Replace: " + str(self.number)
    
    def buy(self, player):
        self.replaceFace(player.dice)
        self.quantity = 0
        player.money -= self.cost

    

    