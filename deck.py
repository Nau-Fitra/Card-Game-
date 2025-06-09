import random
import card

class Deck:
    SUIT_TUPLE = ('Diamonds', 'Clubs', 'Heart', 'Spade')
    STANDARD_DICT = {'Ace': 1, 'Poker': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 12}
    
    def __init__(self, window, rankValueDict=STANDARD_DICT):
        self.startingDeckList = []
        self.playingDeckList = []
        for suit in Deck.SUIT_TUPLE:
            for rank, value in rankValueDict.items():
                ocard = Card(window, rank, suit, value)
                self.startingDeckList.append(ocard)
        self.shuffle()
        
    def shuffle(self):
        self.playingDeckList = self.startingDeckList.copy()
        for ocard in self.playingDeckList:
            ocard.conceal()
        random.shuffle(self.playingDeckList)
    
    def getCard(self):
        if len(self.playingDeckList) == 0:
            raise IndexError('Kartu habis')
        ocard = self.playingDeckList.pop()
        return ocard
        
if __name__ == "__main__":
    
    import pygame
    
    WINDOW_WIDTH = 100
    WINDOW_HEIGHT = 100
    
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    
    odeck = deck(window)
    for i in range(1, 53):
        ocard = odeck.getCard()
        print('Name: ', ocard.getName(), ' value: ', ocard.getValue())