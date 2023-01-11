from art import logo
import random 
import os

############### Blackjack Game Rules (Custom) #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

cards = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}

def Add_Cards():
    """Add new cards to both hands"""
    player_hand.append(random.choice(list(cards.keys())))
    comp_hand.append(random.choice(list(cards.keys())))

def calc_score(hand):
    """Calculates the current score of the player"""
    #score = sum([cards[key] for key in hand])

    score = 0
    values = []
    for key in hand:
        if key == "A":
            if len(hand) > 1 and (score + 11 > 21) :
                values.append(1)
            else:
                values.append(cards[key])
        else:
            values.append(cards[key])

        score = sum(values)
    return score

def score_check(p_score, c_score):
    """Checks the final score and decides the winner"""
    if p_score > 21 :
        print("\nYou went over .. YOU LOSE")
        return
    if c_score == 21 and p_score != 21 :
        print("\nComputer has a Blackjack !! .. YOU LOSE ")
        return
    if p_score == 21 and c_score != 21 :
        print("\nYou have a Blackjack !! .. YOU WIN !! ")
        return
    if p_score <= 21 and c_score <= 21:
        if p_score < c_score:
            print("\nComputer wins .. YOU LOSE \n")
            return
        if p_score > c_score:
            print("\nCongratulations .. YOU WIN !!\n")
            return
        if p_score == c_score:
            print("\nooh .. A DRAW !! ")
            return
    else:
        print("\nCongratulations .. YOU WIN !!")


############## Game #############
while input("\nDo you want to play Blackjack game ? 'y' or 'n' : ").lower() == 'y':
    os.system('cls')
    print(logo)

    player_hand = []
    comp_hand = []
    for i in range(2):
        Add_Cards()
    player_score = calc_score(player_hand)
    comp_score = calc_score(comp_hand)
    while True:
        if comp_score >= 21 or  player_score >= 21:
            break
        else :   # player score < 21
            print(f"\nYour hand : {player_hand}, current score : {player_score}")
            print(f"Computer's first hand : {comp_hand[0]}")

            decision = input("\nType 'y' to get another card, type 'n' to pass : ")
            if decision == 'y':
                Add_Cards()
                player_score = calc_score(player_hand)
                comp_score = calc_score(comp_hand)
                continue
            elif decision == 'n':
                while comp_score < 18:
                    comp_hand.append(random.choice(list(cards.keys())))
                    comp_score = calc_score(comp_hand)
                break
            else:
                print("\nInvalid Input")
                break

    print(f"\nYour final hand : {player_hand}, final score : {player_score}")
    print(f"Computer's final hand : {comp_hand}, Computer's score: {comp_score}")

    score_check(player_score, comp_score)

