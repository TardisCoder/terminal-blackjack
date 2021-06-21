import random
import itertools
from os import system, name

cards = ["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suites = ["♠","♣","♥","♦"]
all_cards = list(x for x in itertools.product(cards, suites))
delt = []
dealerScore = 0
userScore = 0
dealerCards = []
userCards = []
split = False
splitA = []
splitB = []
mainHeader = """
╔══════════════════════════════════════════════════════════════════════════╗
║     ____   _         _      ____  _  __      _     _      ____  _  __    ║
║    | __ ) | |       / \    / ___|| |/ /     | |   / \    / ___|| |/ /    ║
║    |  _ \ | |      / _ \  | |    | ' /   _  | |  / _ \  | |    | ' /     ║
║    | |_) || |___  / ___ \ | |___ | . \  | |_| | / ___ \ | |___ | . \     ║
║    |____/ |_____|/_/   \_\ \____||_|\_\  \___/ /_/   \_\ \____||_|\_\    ║
║                                                                          ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                 WELCOME                                  ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║                                                                          ║
║                                                                          ║
║                                                                          ║
║                                                                          ║
║                                                                          ║
║                                                                          ║
║                                                                          ║
║                                                                          ║
║                                                                          ║
║                                                                          ║
║                                                                          ║
║                                                                          ║
║                                                                          ║
║                                                                          ║
╠══════════════════════════════════════════════════════════════════════════╣
║  Menu:                                                                   ║
║                                                                          ║
║  1. Play New Game                                                        ║
║  2. Exit Game                                                            ║
╚══════════════════════════════════════════════════════════════════════════╝
"""

gameHeader = """
╔══════════════════════════════════════════════════════════════════════════╗
║     ____   _         _      ____  _  __      _     _      ____  _  __    ║
║    | __ ) | |       / \    / ___|| |/ /     | |   / \    / ___|| |/ /    ║
║    |  _ \ | |      / _ \  | |    | ' /   _  | |  / _ \  | |    | ' /     ║
║    | |_) || |___  / ___ \ | |___ | . \  | |_| | / ___ \ | |___ | . \     ║
║    |____/ |_____|/_/   \_\ \____||_|\_\  \___/ /_/   \_\ \____||_|\_\    ║
║                                                                          ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                 WELCOME                                  ║
╠══════════╦═══════════════════════════════════════════════════════════════╣
║          ║                                                               ║
║  Dealer  ║      """

dealerCardsHeader = """
║  Score:  ║      """

dealerScoreHeader = """║    """
# 57 spaces then ║

dealerScoreCardBottoms = """    ║      """

splitGameHeader = """
╔══════════════════════════════════════════════════════════════════════════╗
║     ____   _         _      ____  _  __      _     _      ____  _  __    ║
║    | __ ) | |       / \    / ___|| |/ /     | |   / \    / ___|| |/ /    ║
║    |  _ \ | |      / _ \  | |    | ' /   _  | |  / _ \  | |    | ' /     ║
║    | |_) || |___  / ___ \ | |___ | . \  | |_| | / ___ \ | |___ | . \     ║
║    |____/ |_____|/_/   \_\ \____||_|\_\  \___/ /_/   \_\ \____||_|\_\    ║
║                                                                          ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                 WELCOME                                  ║
╠══════════╦═══════════════════════════════════════════════════════════════╣
║          ║                                                               ║
║  Dealer  ║      ┌----    ┌----    ┌----    ┌----    ┌----    ┌----       ║
║  Score:  ║       A A      A A      A A      A A      A A      A A        ║
║    0     ║      -----    -----    -----    -----    -----    -----       ║
║          ║                                                               ║
╠══════════╬═══════════════════════════════════════════════════════════════╣
║          ║                                                               ║
║          ║      ┌----    ┌----    ┌----    ┌----    ┌----    ┌----       ║
║  Score:  ║       A A      A A      A A      A A      A A      A A        ║
║    0     ║      -----    -----    -----    -----    -----    -----       ║
║          ║                                                               ║
║          ║      ┌----    ┌----    ┌----    ┌----    ┌----    ┌----       ║
║  Score:  ║       A A      A A      A A      A A      A A      A A        ║
║    0     ║      -----    -----    -----    -----    -----    -----       ║
║          ║                                                               ║
╠══════════╩═══════════════════════════════════════════════════════════════╣
║  Moves:                                                                  ║
║    1. Hit       2. Stand      3. Double     4. Split     5. Surrender    ║
╠══════════════════════════════════════════════════════════════════════════╣
║    N. New Game                                           X: Exit Game    ║
╚══════════════════════════════════════════════════════════════════════════╝
"""


regularGameHeader = """
╔══════════════════════════════════════════════════════════════════════════╗
║     ____   _         _      ____  _  __      _     _      ____  _  __    ║
║    | __ ) | |       / \    / ___|| |/ /     | |   / \    / ___|| |/ /    ║
║    |  _ \ | |      / _ \  | |    | ' /   _  | |  / _ \  | |    | ' /     ║
║    | |_) || |___  / ___ \ | |___ | . \  | |_| | / ___ \ | |___ | . \     ║
║    |____/ |_____|/_/   \_\ \____||_|\_\  \___/ /_/   \_\ \____||_|\_\    ║
║                                                                          ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                 WELCOME                                  ║
╠══════════╦═══════════════════════════════════════════════════════════════╣
║          ║                                                               ║
║  Dealer  ║      ┌----    ┌----    ┌----    ┌----    ┌----    ┌----       ║
║  Score:  ║       A A      A A      A A      A A      A A      A A        ║
║    0     ║      -----    -----    -----    -----    -----    -----       ║
║          ║                                                               ║
╠══════════╬═══════════════════════════════════════════════════════════════╣
║          ║                                                               ║
║          ║                                                               ║
║          ║                                                               ║
║  Player  ║      ┌----    -----    -----    -----    -----    -----       ║
║  Score:  ║       A A      A A      A A      A A      A A      A A        ║                                                         ║
║    0     ║      -----    ┌----    ┌----    ┌----    ┌----    ┌----       ║
║          ║                                                               ║
║          ║                                                               ║
║          ║                                                               ║
╠══════════╩═══════════════════════════════════════════════════════════════╣
║  Moves:                                                                  ║
║    1. Hit       2. Stand      3. Double     4. Split     5. Surrender    ║
╠══════════════════════════════════════════════════════════════════════════╣
║    N. New Game                                           X: Exit Game    ║
╚══════════════════════════════════════════════════════════════════════════╝
"""

playerHeaderRegular = """
║          ║                                                               ║
╠══════════╬═══════════════════════════════════════════════════════════════╣
║          ║                                                               ║
║          ║                                                               ║
║          ║                                                               ║
║  Player  ║      """

playerCardsHeader = """
║  Score:  ║      """

playerScoreCardBottoms = """\n║    """
playerAfterScore = """    ║      """

playerHeaderSplit = """
║          ║                                                               ║
╠══════════╬═══════════════════════════════════════════════════════════════╣
║          ║                                                               ║
║          ║      """

gameFooter = """
║          ║                                                               ║
║          ║                                                               ║
║          ║                                                               ║
╠══════════╩═══════════════════════════════════════════════════════════════╣
║  Moves:                                                                  ║
║    1. Hit       2. Stand      3. Double     4. Split     5. Surrender    ║
╠══════════════════════════════════════════════════════════════════════════╣
║    N. New Game                                           X: Exit Game    ║
╚══════════════════════════════════════════════════════════════════════════╝
"""


win = """
╔══════════════════════════════════════════════════════════════════════════╗
║     ____   _         _      ____  _  __      _     _      ____  _  __    ║
║    | __ ) | |       / \    / ___|| |/ /     | |   / \    / ___|| |/ /    ║
║    |  _ \ | |      / _ \  | |    | ' /   _  | |  / _ \  | |    | ' /     ║
║    | |_) || |___  / ___ \ | |___ | . \  | |_| | / ___ \ | |___ | . \     ║
║    |____/ |_____|/_/   \_\ \____||_|\_\  \___/ /_/   \_\ \____||_|\_\    ║
║                                                                          ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                 WELCOME                                  ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║                                                                          ║
║                         __   __                                          ║
║                         \ \ / /  ___   _   _                             ║
║                          \ V /  / _ \ | | | |                            ║
║                           | |  | (_) || |_| |                            ║
║                           |_|   \___/  \__,_|                            ║
║                                                                          ║
║                         __        __ _                                   ║
║                         \ \      / /(_) _ __                             ║
║                          \ \ /\ / / | || '_ \                            ║
║                           \ V  V /  | || | | |                           ║
║                            \_/\_/   |_||_| |_|                           ║
║                                                                          ║
║                                                                          ║
╠══════════════════════════════════════════════════════════════════════════╣
║  Menu:                                                                   ║
║                                                                          ║
║  1. Play New Game                                                        ║
║  2. Exit Game                                                            ║
╚══════════════════════════════════════════════════════════════════════════╝
"""

class blackjack():
    def __init__(self):
     pass

    def cardTop(self):
        return "┌───┐"

    def cardBottom(self):
        return "└───┘"

    def getCard(self):
        global all_cards
        card = random.choice(all_cards)
        a, b = card
        if a != "10":
            abjoined = a + " " + b
        else:
            abjoined = a + b

        if abjoined in delt:
            self.getCard()
        else:
            delt.append(abjoined)

        return (abjoined)

    def getCardValue(self, card):
        if card[0] == "K" or card[0] == "Q" or card[0] == "J" or ((card[0]+card[1]) == "10"):
            return 10
        elif card[0] == "A":
            return 11
        else:
            return int(card[0])

    def getScore(self, player):
        global dealerScore
        global userScore

        if player == "dealer":
            dealerScore = 0
            for x in dealerCards:
                dealerScore += self.getCardValue(x)

        if player == "user":
            userScore = 0
            for x in userCards:
                userScore += self.getCardValue(x)

    def centerScreen(header):
        x, y = os.get_terminal_size()
        width = 72
        spaces = int((x - width) / 2)

        newHeader = ""
        for x in header2:
            newHeader += x
            if x == "\n":
                newHeader = newHeader + ((" ")*spaces)
        return newHeader

    def dealCards(self):

        #deal player
        global userCards
        global dealerScoreCardBottoms
        global playerAfterScore
        global dealerScore
        global userScore

        card = self.getCard()
        userCards.append(card)

        card = self.getCard()
        dealerCards.append(card)

        card = self.getCard()
        userCards.append(card)

        card = self.getCard()
        dealerCards.append(card)

        self.getScore("dealer")
        self.getScore("user")

        if len(str(dealerScore)) == 2:
            dealerScoreCardBottoms = """    ║      """
        else:
            dealerScoreCardBottoms = """     ║      """
        if len(str(userScore)) == 2:
            playerAfterScore = """    ║      """
        else:
            playerAfterScore = """     ║      """

    def checkWin(self):
        global userScore
        global dealerScore
        if userScore == 21 and dealerScore < userScore:
            self.clear()
            print(win)
            cat = input("Select an option: ")
            if cat == "1":
                self.dealCards()
                self.main()
            if cat == "2":
                pass
        elif dealerScore > 21:
            self.clear()
            print(win)
            cat = input("Select an option: ")
            if cat == "1":
                self.dealCards()
                self.main()
            if cat == "2":
                pass
        elif userScore > dealerScore:
            self.clear()
            print(win)
            cat = input("Select an option: ")
            if cat == "1":
                self.dealCards()
                self.main()
            if cat == "2":
                pass
        elif userScore < dealerScore:
            print("you lost.")
        else:
            pass

    def dealHit(self, player):
        global userCards
        global dealerScore
        global userScore
        global dealerScoreCardBottoms
        global playerAfterScore
        if player == "dealer":
            card = self.getCard()
            userCards.append(card)
            self.getScore("dealer")
            if len(str(dealerScore)) == 2:
                dealerScoreCardBottoms = """    ║      """
            else:
                dealerScoreCardBottoms = """     ║      """


        elif player == "user":
            card = self.getCard()
            userCards.append(card)
            self.getScore("user")
            if len(str(userScore)) == 2:
                playerAfterScore = """    ║      """
            else:
                playerAfterScore = """     ║      """


    def clear(self):
        # for windows
        if name == 'nt':
            _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    def split(self):
        split = True
        splitA = userCards[0]
        splitB = userCards[1]

    def main(self):
        self.clear()
        topRowDataDealer = ""
        cardRowDataDealer = ""
        bottomRowDataDealer = ""
        topRowDataUser = ""
        cardRowDataUser = ""
        bottomRowDataUser = ""


        for x in dealerCards:
            topRowDataDealer = topRowDataDealer + self.cardTop() + "    "
        if len(topRowDataDealer) < 57:
            topRowDataDealer = topRowDataDealer + ((" ") * (57-(len(topRowDataDealer)))) + "║"

        for x in dealerCards:
            cardRowDataDealer = cardRowDataDealer + "│" + x + "│    "
        if len(cardRowDataDealer) < 57:
            cardRowDataDealer = cardRowDataDealer + ((" ") * (57-(len(cardRowDataDealer)))) + "║\n"

        for x in dealerCards:
            bottomRowDataDealer = bottomRowDataDealer + self.cardBottom() + "    "
        if len(bottomRowDataDealer) < 57:
            bottomRowDataDealer = bottomRowDataDealer + ((" ") * (57-(len(bottomRowDataDealer)))) + "║"

        if split == False:
            for x in userCards:
                topRowDataUser = topRowDataUser + self.cardTop() + "    "
            if len(topRowDataUser) < 57:
                topRowDataUser = topRowDataUser + ((" ") * (57-(len(topRowDataUser)))) + "║"

            for x in userCards:
                cardRowDataUser = cardRowDataUser + "│" + x + "│    "
            if len(cardRowDataUser) < 57:
                cardRowDataUser = cardRowDataUser + ((" ") * (57-(len(cardRowDataUser)))) + "║"

            for x in userCards:
                bottomRowDataUser = bottomRowDataUser + self.cardBottom() + "    "
            if len(bottomRowDataUser) < 57:
                bottomRowDataUser = bottomRowDataUser + ((" ") * (57-(len(bottomRowDataUser)))) + "║"

            #Change this to a header variable,
            # then pass in the centerScreen function.
            print(gameHeader + topRowDataDealer + dealerCardsHeader + cardRowDataDealer + dealerScoreHeader + str(dealerScore) + dealerScoreCardBottoms + bottomRowDataDealer + playerHeaderRegular + topRowDataUser + playerCardsHeader + cardRowDataUser + playerScoreCardBottoms + str(userScore) + playerAfterScore + bottomRowDataUser + gameFooter)
            self.getInput()

    def getInput(self):
        if userScore == 21 and dealerScore == 21:
            print("Double Blackjack")
        answer = input("Select an option: ")
        if answer == "1":
            self.dealHit("user")
            if dealerScore < 17:
                self.dealHit("dealer")
            elif dealerScore > 17:
                pass

            self.main()

        if answer == "2":
            while dealerScore < 17:
                self.dealHit("dealer")

            if userScore > 21 and dealerScore < 21:
                print("you lost.")
            elif userScore == 21 and dealerScore < userScore:
                self.clear()
                print(win)
                cat = input("Select an option: ")
                if answer == "1":
                    self.dealCards()
                    self.main()
                if answer == "2":
                    pass
            elif dealerScore > 21:
                self.clear()
                print(win)
                cat = input("Select an option: ")
                if answer == "1":
                    self.dealCards()
                    self.main()
                if answer == "2":
                    pass
            elif userScore > dealerScore:
                self.clear()
                print(win)
                cat = input("Select an option: ")
                if answer == "1":
                    self.dealCards()
                    self.main()
                if answer == "2":
                    pass
            elif userScore < dealerScore:
                print("you lost.")



    def intro(self):
        self.clear()
        print(mainHeader)
        answer = input("Select an option: ")
        if answer == "1":
            self.dealCards()
            self.main()
        if answer == "2":
            pass
dog = blackjack()

dog.intro()


#♠ U+2660 Black Spade Suit
#♡ U+2661 White Heart Suit
#♢ U+2662 White Diamond Suit
#♣ U+2663 Black Club Suit
#♤ U+2664 White Spade Suit
#♥ U+2665 Black Heart Suit
#♦ U+2666 Black Diamond Suit
#♧ U+2667 White Club Suit
