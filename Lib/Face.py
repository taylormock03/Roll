# the Generic Face class. All faces will inherit from here
class Face:
    name = ""

    # Special Add-ons
    glued = False
    weighted = False
    reroll =  False
    increment = False
    
    def calculateValue():
        pass

    def __str__(self) -> str:
        return str(self.name)

# This is your typical numeric faces (e.g a 6 on a dice)
class NumberFace(Face):
    number = 0 
    multiplier = 1
    def __init__(self,number):
        self.number = number
        self.name = number

    # This will calculate the values of all basic dice
    # Note that rollFaces is unnecesary for this method, but is used on other faces
    def calculateValue(self,rollFaces,playerBonuses):
        if playerBonuses != []:
            # Passive bonuses have not yet been implemented
            return self.number*self.multiplier*playerBonuses

        else: 
            return self.number*self.multiplier


class DieQuantityMultiplierFace(Face):

    def __init__(self,multiplier):
        self.multiplier = multiplier
        self.name = "Die quantity x" + str(multiplier)

    def calculateValue(self, rollFaces,playerBonuses):
        if playerBonuses == []:
            return self.multiplier*len(rollFaces)

        # Passive bonuses have not yet been implemented
        else:
            return 1
