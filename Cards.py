import random


class card(object):
    def __init__(self,number,suit):
        self.suit = suit
        self.number = number
        self.suits = ["Spades","Clubs","Diamonds","Hearts"]

    def __str__(self):
        if type(self.suit) != int:
            raise ValueError("The suit was not input as an int")
        if type(self.number) != int:
            raise ValueError("The number was not input as an int")
        if self.number > 10:
            faceCards = ["Jack","Queen","King"]
            name = faceCards[self.number-11]
        elif self.number == 1:
            name = "Ace"
        else:
            name = str(self.number)
        suit = self.suits[self.suit]
        return name + " of " + suit
    
    def getSuit(self):
        return self.suits[self.suit]
    def getCard(self):
        if self.number > 10:
            faceCards = ["Jack","Queen","King"]
            name = faceCards[self.number-11]
        elif self.number == 1:
            name = "Ace"
        else:
            name = str(self.number)
        return name
    def getCardNum(self):
        return self.number


class hand(object):

    def __init__(self,numCards,numPlayers):
        self.numCards = numCards
        self.numPlayers = numPlayers

    def createDeck(self):
        cardArr = []
        suitArr = [0,1,2,3]
        for suit in suitArr:
            for i in range(13):
                cardArr.append(card(i+1,suit))
        return cardArr

    def dealHand(self):
        cardArr = self.createDeck()
        hands = []
        for player in range(self.numPlayers):
            hands.append([])

        while len(cardArr) >= self.numPlayers:
            for i in range(len(hands)):
                newCard = cardArr.pop(random.randint(0,len(cardArr)-1))
                hands[i].append(newCard)

        return hands
                


