import random
import sys


class blackjack:

    def __init__(self, decks, initialFunds, playerCount, percentage):
        self.decks = list(range(2, 14) * decks * 4)
        self.money = initialFunds
        self.count = playerCount
        self.percentage = percentage
        self.state = True
        self.cardsPlayed = 0

    def dealCards(self):
        self.playerHand = self.decks[0:2]
        self.houseHand = self.decks[2:4]

        self.decks.extend(self.decks[0:4])
        self.decks = self.decks[4:len(self.decks)]

        blackjack.cardsPlayed += 4

    def printMoney(self):
        print("You have: " + self.money + " $$$$$$$")\


    def getBet(self):
        blackjack.printMoney()

        while (True):
            userInput = input("Enter bet: ")
            self.bet = int(userInput)

            if (blackjack.bet < blackjack.money):
                blackjack.money -= bet
                break

            print("you poor shut up")

        blackjack.printMoney()

    def printHand(self):
        print("Your hand is ", self.playerHand[1:len(self.playerHand) - 1])


if __name__ == '__main__':
    decks = input("How many decks do you want to play: ")
    money = input("How rich you: ")
    count = input("You got friends: ")
    percentage = input("How much you wanna reshuffle: ")

    blackjack = blackjack(decks, money, count, percentage)

    while (True):
        blackjack.dealCards()
        blackjack.getBet()
        blackjack.printHand()


def shuffle():  # shuffles cards
    global deck
    random.shuffle(deck)


def playHand():  # plays a round of blackjack
    global money
    global playing
    global bet
    global deck
    global percentDeckShuffle
    global cardsPlayed
    playing = True
    # print("shuffling every", int(float(len(deck)) * percentDeckShuffle), "cards")
    while playing:
        print("You have", money, "dollars remaining")
        # Player Actions
        displayHands(blackjack.playerHand, blackjack.houseHand)
        naturalCheckDealer(blackjack.houseHand)
        if cardCheck(blackjack.playerHand) == 21:
            print("blackjack!")
            money += bet * 2.5
            playing = False
        while cardCheck(blackjack.playerHand) < 21 and playing:
            print("hit(a), stand(s), double down(d), or surrender(f)")
            print(cardsPlayed, "cards played")
            userInput = input("Enter a, d, or s: ")
            if userInput == "a" or userInput == "s" or userInput == "d" or userInput == "f":
                match userInput:
                    case "a":
                        print("Adding card")
                        cardsPlayed += 1
                        blackjack.playerHand.append(sum(deck[0:1]))
                        deck.extend(deck[0:1])
                        deck = deck[1:len(deck)]
                        displayHands(blackjack.playerHand, blackjack.houseHand)
                        cardsPlayed += 1

                        while cardCheck(blackjack.playerHand) < 21 and playing:
                            print("hit(a) or stand(s)")
                            userInput = input("Enter a or s: ")
                            if cardCheck(blackjack.playerHand) == 21:
                                print("blackjack!")
                                money += bet * 2.5
                                playing = False
                            if userInput == "a":
                                blackjack.playerHand.append(sum(deck[0:1]))
                                deck.extend(deck[0:1])
                                deck = deck[1:len(deck)]
                                displayHands(blackjack.playerHand, blackjack.houseHand)
                                cardsPlayed += 1
                            elif userInput == "s":
                                dealerTurn(blackjack.houseHand)
                                compareCards(blackjack.playerHand, blackjack.houseHand)
                            else:
                                userInput = input("Invalid")
                    case "d":
                        print("Doubling down")
                        if blackjack.money < blackjack.bet:
                            print("You are broke and cannot bet anymore. Cancelling bet")
                            print("hit(a) or stand(s)")
                            userInput = input("Enter a or s: ")
                            if cardCheck(blackjack.playerHand) == 21:
                                print("blackjack!")
                                money += bet * 2.5
                                playing = False
                            if userInput == "a":
                                blackjack.playerHand.append(sum(deck[0:1]))
                                deck.extend(deck[0:1])
                                deck = deck[1:len(deck)]
                                displayHands(blackjack.playerHand, blackjack.houseHand)
                                cardsPlayed += 1
                            elif userInput == "s":
                                dealerTurn(blackjack.houseHand)
                                compareCards(blackjack.playerHand, blackjack.houseHand)
                            else:
                                userInput = input("Invalid")
                        else:
                            money -= bet
                            bet += bet
                            print("You have", money, "dollars remaining")
                            blackjack.playerHand.append(deck[0:1])
                            deck.extend(deck[0:1])
                            deck = deck[1:len(deck)]
                            dealerTurn(blackjack.houseHand)
                            cardsPlayed += 1
                            compareCards(blackjack.playerHand, blackjack.houseHand)
                    case "s":
                        print("Standing")
                        dealerTurn(blackjack.houseHand)
                        compareCards(blackjack.playerHand, blackjack.houseHand)
                    case "f":
                        print("Coward")
                        money += bet / 2
                        bet = 0
                        playing = False
                        break
            else:
                userInput = input("Invalid. Enter a, s, d, or f: ")
        if cardCheck(blackjack.playerHand) > 21:
            print("Bust! :(")
            bet = 0
            playing = False
        if cardsPlayed >= int(float(len(deck)) * percentDeckShuffle):
            shuffle()
            print("shuffling")


def startGame():  # starts the game
    print("Starting the game! Dealer stands on 17 or higher. blackjack pays 1.5x")
    userInput = input("Enter starting money: ")
    global money
    money = int(userInput)


#def displayHands(phand, dhand):  # displays hand info
    #displayblackjack.playerHand = str(phand)
    #displayblackjack.houseHand = str(dhand[0])
    #print("Your hand is ", displayblackjack.playerHand[1:len(displayblackjack.playerHand) - 1])
    #print("Your total:", cardCheck(phand))
    #sys.stdout.write('The house hand is ' + displayblackjack.houseHand + ', ?\n')


def cardCheck(hand):
    testHand = hand

    # normalize 11 to 10
    while testHand.count(11) > 0:
        b = testHand.index(11)
        testHand.insert(b, 10)
        testHand.pop(b + 1)

    # normalize 12 to 10
    while testHand.count(12) > 0:
        n = testHand.index(12)
        testHand.insert(n, 10)
        testHand.pop(n + 1)

    # if sum > 12 && the
    if sum(testHand) > 21 and testHand.count(14) > 0:
        while testHand.count(13) > 0:
            c = testHand.index(13)
            testHand.insert(c, 1)
            testHand.pop(c + 1)
        return sum(testHand)
    elif testHand.count(13) > 0:
        while testHand.count(13) > 0:
            z = testHand.index(13)
            testHand.insert(z, 11)
            testHand.pop(z + 1)
        return sum(testHand)
    else:
        return sum(testHand)


def compareCards(phand, dhand):
    global money
    global bet
    global playing
    if cardCheck(phand) > cardCheck(dhand):
        money += bet * 2
        print("You won!!!")
        playing = False
    elif cardCheck(phand) == cardCheck(dhand):
        print("You drew")
        money += bet
        playing = False
    else:
        print("You lost")
        bet = 0
        playing = False


def dealerTurn(dhand):
    while cardCheck(dhand) < 17:
        dhand.append(sum(deck[0:1]))
        deck.extend(deck[0:1])
        deck = deck[1:len(deck)]
    print("The dealers hand is", displayblackjack.houseHand[1:len(displayblackjack.houseHand) - 1])


def naturalCheckDealer(dhand):
    global bet
    global playing
    if cardCheck(dhand) == 21:
        print("Dealer has blackjack. You lose")
        bet = 0
        playing = False


class aiPlayer:
    aiHand = []

    def __init__(self, name):
        self.name = name

    def aihanddeal(self):
        global deck
        aiHand = deck[0:2]
        deck.extend(deck[0:2])
        deck = deck[2:len(deck)]
        displayaiHand = str(aiHand)
        print(self.name, "has the hand", displayaiHand[1:len(displayaiHand) - 1])


while True:  # gets percentage to shuffle the deck at
    userInput = input("Enter percent to shuffle deck at in decimal form: ")
    percentDeckShuffle = float(userInput)
    if percentDeckShuffle < .2:
        userInput = input("Enter percentage(>=.2) to shuffle deck at in decimal form: ")
        percentDeckShuffle = float(userInput)
        print("Must be .2 or greater")
    elif percentDeckShuffle >= .2:
        break
while True:  # generates ai players
    userInput = input("Input number of AI players: ")
    playercount = int(userInput)
    if playercount < 0:
        print("Player count cannot be lower than 0")
        userInput = input("Input number of AI players: ")
        playercount = int(userInput)
    else:
        playerNamesNum = []
        for x in range(playercount):
            print(names[x], "is playing")
            playerNamesNum.append('player' + str(x))
            playerNamesNum[x] = aiPlayer(names[x])
    break


shuffle()
startGame()
while blackjack.money > 0 or playing:
    playHand()
print("You went bankrupt :(")
