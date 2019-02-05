import random

class card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.val = self.rank2Val(rank)

    def rank2Val(self, rank):
        if type(rank) is int:
            return rank
        if rank in ['Jack', 'Queen', 'King']:
            return 10
        if rank == 'Ace':
            return 11
        return -1

class player:
    def __init__(self, name):
        self.cards = []
        self.name = name
    def getSum(self, dealerCardDown):
        sum = 0
        aces = 0
        cards = self.cards
        if dealerCardDown: cards = cards[1:]
        for card in cards:
            if(card.val == 11): aces += 1
            sum += card.val
        while(sum > 21):
            if (aces > 0):
                sum -= 10
                aces -= 1
            else: break
        return sum
    def clearCards(self):
        self.cards = []

class deck:
    def __init__(self, numDecks):
        self.numDecks = numDecks
        self.cards = self.getNewDeck()
        self.cardsDrawn = 0
        self.cardsLeft = len(self.cards)

    def getNewDeck(self):
        cards = []
        numDecks = self.numDecks
        for i in range(1, numDecks+1):
            for suit in ['Diamonds','Hearts','Spades','Clubs']:
                for rank in range (2,11):
                    cards.append(card(suit, rank))
                for rank in ['Jack', 'Queen','King', 'Ace']:
                    cards.append(card(suit, rank))
        random.shuffle(cards)
        return cards

    def shuffleDeck(self):
        print('Shuffling cards...')
        self.cards = self.getNewDeck()
        self.cardsDrawn = 0
        self.cardsLeft = len(self.cards)

    def drawCard(self):
        if (self.cardsLeft > 0):
            cardDrawn = self.cards.pop()
            self.cardsDrawn += 1
            self.cardsLeft -= 1
            return cardDrawn
        else:
            self.shuffleDeck()
            return self.drawCard()
