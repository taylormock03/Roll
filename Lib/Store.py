from random import randint
from Lib.Upgrades import *
# This is represents how many types of upgrades there are. 
# I don't know if there is a way to dynamically generate this number 
# based on the number of child classes of Upgrade
NUM_UPGRADE_TYPES = 0

class Store:
    def __init__(self,player):
        self.level = 1
        self.refreshes = 0
        self.refreshStock(player)

    def refreshStock(self,player):
        # This will choose (2*the level of the store + 2) items
        # e.g if store = level3, it will select 2*3+2 = 8 items
        self.stock=[]
        for x in range(0,3+self.level*2):
            itemId = randint(0,NUM_UPGRADE_TYPES)

            if itemId ==0:
                self.stock.append(FaceReplaceUpgrade(randint(10,100), 
                                                        self.level,
                                                        self.refreshes))
    
    def viewStore(self,player):
        i=1
        print()
        for x in self.stock:
            print("Item #" +str(i) + "\n"+ str(x))
            i+=1
        
        print("You have $" + str(player.money))

        playerInput = input("Would you like to buy something (y/n)? \n> ")
        if playerInput == "y":
            self.buyStore(player)

    def buyStore(self,player):
        # try:
            playerInput = int(input("What number item would you like?\n>"))-1

            if self.stock[playerInput].cost<= player.money and self.stock[playerInput].quantity>0:
                self.stock[playerInput].buy(player)
            else:
                raise
        # except: 
        #     print("Error - invalid stock item chosen (check if it is in stock and you have enough money)")
