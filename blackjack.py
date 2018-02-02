import random

totalChip = 100
userInputChip = 0
ranking = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
card_val = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}

def heading():
    print 'Welcome to BlackJack'


def askUserBet():
    global userInputChip
    global totalChip

    while userInputChip == 0:
        bet = eval(raw_input('Enter your betting'))
        if bet > 0 and bet < totalChip:
            userInputChip = bet
        else:
            print 'You Entered Invalid bet amount'


class Deck():

    def __init__(self):
        self.deck = []
        for rank in ranking:
            self.deck.append(rank)

    def shuffle(self):
        random.shuffle(self.deck)

    def getCard(self):
        return self.deck.pop()

    def printDeck(self):
        print self.deck


class Player():
    global card_val

    def __init__(self):
        self.userCard = []
        self.count = 0

    def addCard(self, card):
        self.userCard.append(card)

    def countCard(self):
        self.count = 0
        for card in self.userCard:
            if card == 'A' and self.count < 12:
                self.count += 11
            else:
                self.count += card_val[card]

    def getPlayerCard(self):
        return self.userCard

    def getcountPlayerCard(self):
        return self.count


def dealCards():
    global deck, userPlayer, dealer

    deck = Deck()
    deck.shuffle()

    askUserBet()

    userPlayer = Player()
    dealer = Player()

    userPlayer.addCard(deck.getCard())
    userPlayer.addCard(deck.getCard())

    dealer.addCard(deck.getCard())
    dealer.addCard(deck.getCard())

    printCards(hidden=True)
    print 'Do you want to Hit or Stand. Press H or S'
    askInput()


def printCards(hidden):
    userPlayer.countCard()
    dealer.countCard()
    print 'Player Cards Count : %s' % userPlayer.getcountPlayerCard()
    for card in userPlayer.getPlayerCard():
        print '--------'
        print '|      |'
        print '   %s' % card
        print '|      |'
        print '--------'

    if hidden == True:
        print 'Dealer Cards'
    else:
        print 'Dealer Cards Count : %s' % dealer.getcountPlayerCard()

    for card in dealer.getPlayerCard():
        print '--------'
        print '|      |'
        print '   %s' % card
        print '|      |'
        print '--------'

        if hidden == True:
            break


def askInput():
    val = raw_input().lower()

    if val == 'h':
        hit()
    elif val == 's':
        stand()
    elif val == 'd':
        dealCards()
    elif val == 'q':
        exit()


def hit():
    global userPlayer, dealer, userInputChip, deck, totalChip

    userPlayer.addCard(deck.getCard())
    userPlayer.countCard()

    if userPlayer.getcountPlayerCard() > 21:
        print 'You have busted. Press d to deal again or q to quit'
        totalChip -= userInputChip
        print 'Total Chip Value %s' % totalChip
        printCards(hidden=False)
        askInput()
    else:
        printCards(hidden=True)
        print 'Do you want to Hit or Stand. Press H or S'
        askInput()


def stand():
    global deck, dealer, userPlayer, totalChip, userInputChip

    dealer.countCard()

    while dealer.getcountPlayerCard() < 17:
        dealer.addCard(deck.getCard())
        dealer.countCard()

    if dealer.getcountPlayerCard() > 21:
        totalChip += userInputChip
        printCards(hidden=False)
        print 'Dealer Busted. Player wins. Press d to deal again or q to quit'
        print 'Total Chip Value %s' % totalChip
        askInput()
    elif dealer.getcountPlayerCard() < userPlayer.getcountPlayerCard():
        totalChip += userInputChip
        printCards(hidden=False)
        print 'Player Wins. Press d to deal again or q to quit'
        print 'Total Chip Value %s' % totalChip
        askInput()
    elif dealer.getPlayerCard() == userPlayer.getcountPlayerCard():
        printCards(hidden=False)
        print 'Push. Press d to deal again or q to quit'
        print 'Total Chip Value %s' % totalChip
        askInput()
    else:
        totalChip -= userInputChip
        printCards(hidden=False)
        print 'Dealer Wins. Press d to deal again or q to quit'
        print 'Total Chip Value %s' % totalChip
        askInput()


userPlayer = Player()
dealer = Player()
deck = Deck()
heading()
dealCards()