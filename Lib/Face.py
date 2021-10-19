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
        self.name = "Die Quantity Multiplier x" + str(multiplier)

    def calculateValue(self, rollFaces,playerBonuses):
        if playerBonuses == []:
            return self.multiplier*len(rollFaces)

        # Passive bonuses have not yet been implemented
        else:
            return 1

class SingleFaceMultiplerFace(Face):
    def __init__(self,multiplier):
        self.multiplier = multiplier
        self.name = "Single Face Multiplier x" + str(multiplier)

    def calculateValue(self, rollFaces,playerBonuses):
        highestValue = 0
        # calculate the highest Face rolled
        for x in rollFaces:
            # check if a face is a numeric face
            if isinstance(x, NumberFace):
                if x.number>highestValue:
                    highestValue = x.number


        if playerBonuses == []:
            return self.multiplier*highestValue

        # Passive bonuses have not yet been implemented
        else:
            return 1

# multiples the most common face that has been rolled by a multiplier
class MultiFaceMultiplerFace(Face):
    def __init__(self,multiplier):
        self.multiplier = multiplier
        self.name = "Multi Face Multiplier x" + str(multiplier)

    def calculateValue(self, rollFaces,playerBonuses):
        values ={} 
        # calculate the quantity of every Face rolled
        for x in rollFaces:
            # check if a face is a numeric face
            if isinstance(x, NumberFace):
                try:
                    values[x.number]+=1
                except:
                    values[x.number]=1

        # calculate the most frequent face
        frequentValue = 0
        for x in values:
            if x>frequentValue:
                frequentValue = x
        if playerBonuses == []:
            return self.multiplier*frequentValue

        # Passive bonuses have not yet been implemented
        else:
            return 1