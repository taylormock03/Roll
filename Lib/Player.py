from Lib.Dice import Dice


class Player:
    money = 0
    noRolls = 0
    dice = []
    passiveBonuses = [] 

    def __init__(self):
        # Choose the number of times you can roll a dice (the original game uses 2500 as its base (and only) value)
        while self.noRolls == 0:
            try:
                self.noRolls = int(input("How many rolls would you like? \n> "))
            except:
                print("Error - Invalid number")
        
        self.dice.append(Dice())
        self.passiveBonuses = []

    # Roll the dice once and calculate output
    # Note: the output is only for when the user chooses to roll once
    def roll(self, output=True):
        rollFaces = []
        # Find which face was rolled for each dice 
        for x in self.dice:
            rollFaces.append(x.roll())
        
        # Calculate the value of each dice
        totalGain = 0
        if output:
            print("\nYou rolled: ")
        for face in rollFaces:
            if output:
                print(face)
            totalGain += face.calculateValue(rollFaces,self.passiveBonuses)
            self.money += totalGain
        if output:
            print("\nYou earned: $" +str(totalGain)+"\n")
        self.noRolls-=1
        
        # This is only used when the player rolls multiple times
        return totalGain

    # Rolls the dice until the player reaches the amount of money they specify or they run out of rolls
    def rollUntil(self, moneyLimit):
        moneyLimit=int(moneyLimit)
        
        i = 0
        totalGain = 0
        while self.money<moneyLimit and self.noRolls>0:
            totalGain += self.roll(output=False)
            i+=1
        
        print("\nYou rolled: " + str(i) + " times")
        print("You gained: $" + str(totalGain))


    # Rolls the dice X times
    def rollX(self, rollLimit):
        print()
        rollLimit=int(rollLimit)

        if rollLimit > self.noRolls:
            print("You don't have enough rolls to do that")
            return

        i = 0
        totalGain = 0
        while i< rollLimit:
            totalGain += self.roll(output=False)
            i+=1
        print("You rolled: " +str(rollLimit)+" times\nYou earned: $" +str(totalGain))