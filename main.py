import random


deck = []
players = {}
playerHand = [[]]

class Card:
    """
    Class modelling a standard deck card.
    """
    def __init__(self, value, color):
        self.value = value
        self.color = color

def create_deck():
    """
    Generates a Hollywood card deck. Consists of two standard card decks.

    :return: A deck of cards
    """
    colors = ['hearts', 'diamonds', 'clubs', 'spades']
    dck = [Card(value, color) for value in range(1, 14) for color in colors]
    dck = dck + dck
    return dck

def init_game():
    """
    Initialises the game by selecting number of opponents, and giving them standard names.

    :return:
    """
    playerNames = ['Player1', 'Alice', 'Bob', 'Charlie']

    # User input of no. of opponents.
    opponents = int(raw_input("Enter number of opponents (max 3): "))
    while opponents not in range(0,4):
        opponents = int(raw_input("Let's try this again, shall we? Please enter the number of desired opponents (max 3): "))

    playerNo = opponents + 1 # Adding Player1
    players = {str(x):playerNames[x] for x in range(0,opponents+1)}

    deck = create_deck() # Creates a deck...
    random.shuffle(deck) # ...and shuffles it.

    print("Shuffling the deck...")

    for i in range(0,11): # Every player shall start with 10 cards on hand
        for j in range(0, playerNo):
            card = deck.pop(0) # Take top-most card of deck...
            playerHand[j].append(card) # ...and put it in a player's hand.

    print("Handing out cards...")





if __name__ == "__main__":
    while True:
        quit = raw_input("Welcome to HollPyWood card game! \n\nDo you want or play or quit? (p/q): ")
        if quit == "p":
            init_game()
        else:
            break

    print("Exited HollPyWood!\n")
