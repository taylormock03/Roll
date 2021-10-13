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

    def roll(self):
        rollFaces = []
        # Find which face was rolled for each dice 
        for x in self.dice:
            rollFaces.append(x.roll())
        
        # Calculate the value of each dice
        totalGain = 0
        for face in rollFaces:
            totalGain += face.calculateValue(rollFaces,self.passiveBonuses)
            self.money += totalGain
        print(totalGain)
        self.noRolls-=1