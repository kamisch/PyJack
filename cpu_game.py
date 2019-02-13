from model import deck
from model import card
from model import player

import pdb, sys
import random
import csv

numDecks = 1

dealer = player('Dealer')
gambler = player('Player')
gamesWon = 0
gamesPushed = 0
totalGames = 0
d1 = deck(numDecks)

def main():
    global gamesWon, gamesPushed, totalGames
    gameDone = False
    datasetSize = 1000000
    count = 0 
    while not gameDone:
        count += 1
        print(count)
        if count == datasetSize:
            gameDone = True
        dealerInfo = ["dealer"]
        playerInfo = ["player"]
        gameResult = runHand(dealer, gambler)
        for x in dealer.cards:
            dealerInfo.append(x.rank)
        for y in gambler.cards:
            playerInfo.append(y.rank)
        if gameResult == 1:
            gamesWon += 1
            #print('The gambler won the hand!')
            playerInfo.append(1)
            dealerInfo.append(-1)
        elif gameResult == 0:
            gamesPushed += 1
            #print('Push... Lame!')
            playerInfo.append(0)
            dealerInfo.append(0)
        else: 
            #print('The gambler lost the hand. Bummer :(')
            playerInfo.append(-1)
            dealerInfo.append(1)
        with open('./result.csv',"a",newline='') as csvFile:
            csvWriter = csv.writer(csvFile,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
            csvWriter.writerow(playerInfo)
            csvWriter.writerow(dealerInfo)

        playerInput = "y"

        while playerInput.strip().lower() not in ['y','n','yes','no']:
            playerInput = input('Input not recognized. Enter "yes"/"y" to keep playing this game or "no"/"n" to finish the game: ')

        if playerInput in ['no','n']:

            #print('Game ended. -- Games played: {0} -- Games won: {1} -- Games pushed: {2}'.format(totalGames, gamesWon, gamesPushed))
            playerInput = input('Play again? (y/n): ')

            while playerInput not in ['y','n','yes','no']:
                playerInput = input('Input not recognized. Enter "yes"/"y" to play again or "no"/"n" to quit:')
            if playerInput in ['n', 'no']:
                gameDone = True
            else:
                reset()


def runHand(dealer, gambler):
    global totalGames
    totalGames += 1

    dealer.clearCards()
    gambler.clearCards()

    dealer.cards.append(d1.drawCard())
    dealer.cards.append(d1.drawCard())

    gambler.cards.append(d1.drawCard())
    gambler.cards.append(d1.drawCard())

    if gambler.getSum(False) == 21:
        #print('Gambler has blackjack! Gambler wins')
        return 1

    if dealer.cards[1].val >= 10 and dealer.getSum(False) == 21:
        printPlayerInfo(dealer, False)
        #print('Dealer has blackjack. Gambler looses.')
        return -1

    printPlayerInfo(dealer, True)

    playerScore = playHand(gambler, False)
    if playerScore == -1:
        return -1

    dealerScore = playHand(dealer, True)

    if dealerScore == playerScore: return 0
    elif playerScore > dealerScore: return 1
    else: -1

def playHand(player, isDealer):
    # if isDealer: pdb.set_trace()

    sum = player.getSum(False)

    if sum > 21:
        #print('{0} busts with {1}.'.format(player.name, sum))
        return -1

    printPlayerInfo(player, False)

    if sum == 21:
        return sum

    if isDealer:
        if sum < 17:
            #print('Dealer hits on {0}'.format(sum))
            player.cards.append(d1.drawCard())
            return playHand(player, True)
        else: return sum
    else:
        base = 10
        base = base + random.randint(1,8)
        if sum < base:
            #print('Player hits on {0}'.format(sum))
            player.cards.append(d1.drawCard())
            return playHand(player,False)
        else: return sum
    #playerInput = input('Hit or Stay? (h/s): ')
    #while(playerInput.strip().lower() not in ['h', 's', 'hitt', 'stay']):
    #    playerInput = input('Input not recognized. Enter "hit"/"h" to hit or stay"/"s" to stay: ')

    #if playerInput.strip().lower() in ['h','hitt']:
    #    player.cards.append(d1.drawCard())
    #   return playHand(player, False)

    #return sum

def printPlayerInfo(player, cardDown):
    cards = player.cards
    sum = player.getSum(cardDown)

    if cardDown:
        cards = cards[1:]

    #print('{0} is showing:'.format(player.name), end='')
    #if cardDown: 
        #print(' *down card hidden*', end='')
    #print(' {0}'.format(cards[0].rank), end='')
    #for card in cards[1:]:
        #print(', {0}'.format(card.rank), end='')
    #print(' -- Value: {}'.format(sum))
def reset():
    global d1, gamesWon, gamesPushed, totalGames
    d1 = deck(numDecks)
    gamesWon = 0
    gamesPushed = 0
    totalGames = 0


if __name__ == '__main__':
    main()
