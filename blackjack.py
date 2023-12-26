# COPYRIGHT 2022 MATT SERDUKOFF
# BLACKJACK GAME by Matt Serdukoff

import random
import sys

# constants for cards display
HEARTS = chr(9829) # ♥
DIAMONDS = chr(9830) # ♦
SPADES = chr(9824) # ♠
CLUBS = chr(9827) # ♣

BACKSIDE = 'backside'

def main():
    print("BLACKJACK by Matt Serdukoff")

    money = 10000
    # main loop
    while True:
        if money <=0:
            print("You're a brokie! Leave the casino at once!")
            sys.exit()
        print('Money: ', money)
        bet = get_bet(money)

        # give player & dealer 2 cards
        deck = get_deck()
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]

        # handling player actions
        print('Bet: ', bet)
        while True:
            displayHands(player_hand, dealer_hand, False)
            print()

            # check for bust
            if getHandVal(player_hand) > 21:
                break

            # get player move 
            move = get_move(player_hand, money - bet)

            # handling actions
            if move == 'D':
                added_bet = get_bet(min(bet, (money - bet)))
                bet += added_bet
                print('Bet increased to {}.'.format.bet())
                print('Bet:', bet)
            if move in ('H', 'D'):
                new_card = deck.pop()
                rank, suit = new_card
                print('You drew {} of {}'.format(rank, suit))
                player_hand.append(new_card)
                
                if getHandVal(player_hand) > 21:
                    continue
            if move in ('S', 'D'):
                break
        if getHandVal(player_hand) <= 21:
            while getHandVal(dealer_hand) < 17:
                print('Dealer hits...')
                dealer_hand.append(deck.pop())
                displayHands(player_hand, dealer_hand, False)

                if getHandVal(dealer_hand) > 21:
                    break
                input('Press Enter to continue.\n\n')

        displayHands(player_hand, dealer_hand, True)
        player_val = getHandVal(player_hand)
        dealer_val = getHandVal(dealer_hand)

        if dealer_val > 21:
            print('Dealer busts! You win ${}!'.format(bet))
            money += bet
        elif (player_val > 21) or (player_val < dealer_val):
            print('You lost!')
            money -= bet
        elif player_val > dealer_val:
            print('You win ${}!'.format(bet))
            money += bet
        elif player_val == dealer_val:
            print('Its a tie, bet returned.')
            print('Press Enter to continue.\n\n')


# function definitions
def get_bet(MAX_BET):
    while True:
        print('How much are you betting? (1-{}, or QUIT)'.format(MAX_BET))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print("Thank you for playing.")
            sys.exit()
        if not bet.isdecimal():
            continue
        bet = int(bet)
        if 1 <= bet <= MAX_BET:
            return bet

def get_deck():
    deck = []
    # filling the deck
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2,11):
            deck.append((str(rank),suit))
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank,suit))
    random.shuffle(deck)
    return deck

def displayHands(playerHand, dealerHand, showDealerHand):
    print()
    
    if showDealerHand:
        print('DEALER:', getHandVal(dealerHand))
        display_cards(dealerHand)
    else:
        print('DEALER: ???')
        display_cards([BACKSIDE] + dealerHand[1:])
    print('PLAYER:', getHandVal(playerHand))

def getHandVal(cards):
    val = 0
    num_aces = 0

    for card in cards:
        rank = card[0] # (rank suite)
        if rank == 'A':
            num_aces += 1
        elif rank in ('K', 'Q', 'J'):
            val += 10
        else:
            val += int(rank)
        
    val += num_aces
    for i in range(num_aces):
        if val + 10 <= 21:
            value += 10
    
    return val

def display_cards(cards):
    rows = ['','','','','']

    for i, card in enumerate(cards):
        rows[0] += ' __  '
        if card == BACKSIDE:
            # print back side
            rows[1] += '|## |'
            rows [2] += '|###|'
            rows [3] += '| ##|'
        else:
            rank, suit = card
            rows[1] += '|{} |'.format(rank.ljust(2))
            rows[2] += '| {} |'.format(suit)
            rows[3] += '|_{}|'.format(rank.rjust(2,'_'))
    
    for row in rows:
        print(row)

def get_move(playerHand, money):
    while True:
        moves = ['(H)it', '(S)tand']
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')
        move_prompt = ', '.join(moves) + '> '
        move = input(move_prompt).upper()
        if move in ('H', 'S'):
            return move
        if move == 'D' and '(D)ouble down' in moves:
            return move

if __name__ == '__main__':
    main()
