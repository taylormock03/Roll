from random import randint
from Lib.Upgrades import *
# This is represents how many types of upgrades there are. 
# I don't know if there is a way to dynamically generate this number 
# based on the number of child classes of Upgrade
NUM_UPGRADE_TYPES = 3

class Store:
    def __init__(self):
        self.level = 0
        self.refreshes = 0
        self.refreshStock()
        self.refreshCost()
        self.upgradeCost()

    # This will add new upgrades into stock
    def refreshStock(self):
        # This will choose (2*the level of the store + 2) items
        # e.g if store = level3, it will select 2*3+2 = 8 items
        self.stock=[]
        for x in range(0,max(2+self.level*2,4)):
            itemId = randint(1,NUM_UPGRADE_TYPES)

            if itemId ==1:
                self.stock.append(NumberReplaceUpgrade(randint(10,100), 
                                                        self.level,
                                                        self.refreshes))

            elif itemId ==2:
                self.stock.append(NumberAddUpgrade(randint(10,100), 
                                                        self.level,
                                                        self.refreshes))

            elif itemId ==3:
                self.stock.append(Incrementor(randint(10,100), 
                                                        self.level,
                                                        self.refreshes))

    # This will calculate the cost of a shop refresh
    def refreshCost(self):
        self.refreshPrice = max(100*self.level*self.refreshes,100)
        self.refreshes+=1

    # This will calculate the cost of upgrading the store
    def upgradeCost(self):
        self.upgradePrice = max(500*self.level*self.refreshes,500)
        self.level+=1

    def viewStore(self,player):
        i=1
        print()
        for x in self.stock:
            print("Item #" +str(i) + "\n"+ str(x))
            i+=1
        
        print("Item #" +str(i) + "\nStore refresh\nCost: $" + str(self.refreshPrice))

        print("\nItem #" +str(i+1) + "\nStore Upgrade\nCost: $" + str(self.upgradePrice))

        print("\nYou have $" + str(player.money))

        playerInput = input("Would you like to buy something (y/n)? \n> ")
        if playerInput == "y":
            self.buyStore(player)

    def buyStore(self,player):
        try:
            playerInput = int(input("What number item would you like?\n> "))-1

            if playerInput==len(self.stock) and player.money>= self.refreshPrice:
                self.refreshStock()
                self.refreshCost()
                player.money -= self.refreshPrice
                print("Store refreshed")
            
            elif playerInput==len(self.stock)+1 and player.money >= self.upgradePrice:
                self.upgradeCost()
                self.refreshCost()
                self.refreshStock()
                player.money -= self.upgradePrice
                print("Store upgraded and refreshed")

            elif self.stock[playerInput].cost<= player.money and self.stock[playerInput].quantity>0:
                self.stock[playerInput].buy(player)
            
            else:
                raise
        except: 
            print("Error - invalid stock item chosen (check if it is in stock and you have enough money)")
