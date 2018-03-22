import random


deck = []
players = {}
playerNo = 0
playerHand = [[]]
round = ['tt','tS','SS','ttt','sss','ttS']

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

def start_game():
    order = range(0, playerNo)
    turn = 0
    finished = False
    currentCard = deck.pop(0)

    while not finished:
        if turn == 0: # Player1's turn
            print("Current card: " + currentCard.color + ", " + str(currentCard.value))
            ans = raw_input("Pick this card or a random card off the deck? (T/R): ")
            if ans == 'T':
                playerHand[0].sort()
                print("Choose a card to discard!")
                for i in len(playerHand[0]):
                    print(str(i) + ": " + currentCard.color + ", " + str(currentCard.value) + "\n")
                choice = str(raw_input("Choice: "))

                playerHand[0].pop(i+1) # Discard chosen card (+1 to fix off-by-one error)
            Pick
        else: # AI players' turns.


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
    print("Lets play!")

    start_game()


if __name__ == "__main__":
    while True:
        quit = raw_input("Welcome to HollPyWood card game! \n\nDo you want or play or quit? (p/q): ")
        if quit == "p":
            init_game()
        else:
            break

    print("Exited HollPyWood!\n")
