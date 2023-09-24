import random, sys

Hearts = chr(9829)
Diamonds = chr(9830)
Spades = chr(9824)
Clubs = chr(9827)

Backside = 'backside'


def main():
    print('Welcome To Blackjack')

    money = 5000

    while True:
        if money <= 0:
            print("No money left \n Thanks for Playing!")
            sys.exit()

        print(f"Starting Cash: {money}")
        bet = getBet(money)

        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        print('Bet:', bet)
        while True:
            displayHands(playerHand, dealerHand, False)
            print()

            if getHandValue(playerHand) >21:
                break

            move = getMove(playerHand, money - bet)

            if move == 'D':
                addutionalBet = getBet(min(bet, (money-bet)))
                bet += addutionalBet
                print(f"Bet increased to {bet}")

            if move in ('H', 'D'):
                newCard = deck.pop()
                rank, suit = newCard
                print(f"You drew a {rank} of {suit}")
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    continue

            if move in ('S', 'D'):
                break

        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                print("Dealer Hits")
                dealerHand.append(deck.pop())
                displayHands(playerHand,dealerHand,False)

                if getHandValue(dealerHand) > 21:
                    break
                input("Enter to continue")
                print('\n\n')

        displayHands(playerHand,dealerHand,True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)

        if dealerValue > 21:
            print(f'Dealer busts! you win ${bet}')
            money += bet
        elif dealerValue > playerValue or playerValue > 21:
            print(f'You lost ${bet}')
            money -= bet
        elif playerValue > dealerValue:
            print(f"You won ${bet}")
            money += bet
        elif dealerValue == playerValue:
            print('Its a Draw!')

        print(f"\n money: {money}")
        input('Press Enter to continue')
        print('\n\n')

def getBet(maxBet):
    while True:
        print('How much money to bet this round?, or type QUIT to exit')
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            sys.exit()

        if not bet.isdecimal():
            continue

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet

def getDeck():
    deck = []
    for suit in (Hearts, Diamonds, Spades, Clubs):
        for rank in range(2,11):
            deck.append((str(rank), suit))
        for rank in ('J','Q','K','A'):
            deck.append((rank,suit))
        random.shuffle(deck)
        return deck

def displayHands(playerHand, dealerHand, showDealerHand):
    print()
    if showDealerHand:
        print(f"Dealer: {getHandValue(dealerHand)}")
        displayCards(dealerHand)
    else:
        print('Dealer: ???')
        displayCards([Backside] + dealerHand[1:])

    print('YOU:', getHandValue(playerHand))
    displayCards(playerHand)

def getHandValue(cards):
    value = 0
    numberOfAces = 0

    for card in cards:
        rank = card[0]
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K','Q','J'):
            value += 10
        else:
            value += int(rank)

    value += numberOfAces
    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10

    return value

def displayCards(cards):
    rows = ["", "", "", "", ""]

    for i, card in enumerate(cards):
        rows[0] += '  ___ '
        if card == Backside:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            rank, suit = card
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    for row in rows:
        print(row)

def getMove(playerHand, money):
    while True:
        moves = ['(H)it', '(S)tand']

        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble Down')

        move = input("Enter Move: ")
        if move in ('H', 'S'):
            return move
        if move == 'D' and '(D)ouble Down' in moves:
            return move

if __name__ == '__main__':
    main()