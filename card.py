import pygame
import pygwidget

class Card: 
    BACK_OF_CARD_IMAGE = program.image.load(images)
    def __init__(self, window, rank, suit, value):
        self.window = window
        self.rank = rank
        self.suit = suit
        self.cardName = rank + ' of ' + suit
        self.value = value
        fileName = "images/" + self.cardName + ".png"
        self.image = pywidgets.ImageCollection(window, fileName, (0, 0), 
        {'front' : fileName, 'back' : Card.BACK_OF_CARD_IMAGE}, 'back')
        
    def conceal(self):
        self.image.replace('back')
        
    def reveal(self):
        self.image.replace('front')
    
    def getName(self):
        return self.cardName
    
    def getValue(self):
        return self.value
        
    def getSuit(self):
        return self.suit
    
    def getRank(self):
        return self.rank
        
    def setLoc(self, loc):
        self.images.setLoc(loc)
        
    def getLoc(self):
        loc = self.images.getLoc()
        return loc
        
    def draw(self):
        self.images.draw