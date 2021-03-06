from Lib.Face import *

from random import randint
# This is the class that has the dice
# It will store all faces and calculate the
# result of rolls
class Dice:
    # This is where each of the 6 die faces are stored
    

    # By default a die will be created with 6 faces between 1 and 6 (normal dice)
    def __init__(self, diceFaces=[1,2,3,4,5,6]):
        self.faces = []
        for x in diceFaces:
            self.faces.append(NumberFace(x))

    # Chooses a random 
    def roll(self):
        return self.faces[randint(0,5)]

    def __str__(self):
        faceList="[" 
        for x in self.faces:
            faceList+= str(x)+", "
        faceList+= "]"

        return faceList

    def setFace(self, pos, newFace):
        self.faces[pos] = newFace