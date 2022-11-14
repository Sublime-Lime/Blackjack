import random
import sys


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
        # deals cards
        # print(deck)
        playerHand = deck[0:2]
        houseHand = deck[2:4]
        deck.extend(deck[0:4])
        deck = deck[4:len(deck)]
        cardsPlayed += 4
        # print(deck)
        # print(playerHand)
        # print(houseHand)
        # Places and validates bet
        print("You have", money, "dollars")
        userInput = input("Enter bet: ")
        bet = int(userInput)
        if bet <= money:
            money -= bet
        else:
            print("Bet exceeds balance. Try again")
            while bet > money:
                userInput = input("Enter bet: ")
                bet = int(userInput)
                money -= bet
        print("You have", money, "dollars remaining")
        # Player Actions
        displayHands(playerHand, houseHand)
        while cardCheck(playerHand) < 21 and playing:
            print("hit(a), stand(s), double down(d), or surrender(f)")
            print(cardsPlayed)
            userInput = input("Enter a, d, or s: ")
            if userInput == "a" or userInput == "s" or userInput == "d" or userInput == "f":
                match userInput:
                    case "a":
                        print("Adding card")
                        cardsPlayed += 1
                        playerHand.append(sum(deck[0:1]))
                        displayHands(playerHand, houseHand)
                        while cardCheck(playerHand) < 21 and playing:
                            print("hit(a) or stand(s)")
                            userInput = input("Enter a or s: ")
                            if userInput == "a":
                                playerHand.append(sum(deck[0:1]))
                                deck.extend(deck[0:1])
                                deck = deck[1:len(deck)]
                                displayHands(playerHand, houseHand)
                                cardsPlayed += 1
                            elif userInput == "s":
                                dealerTurn(playerHand, houseHand)
                                compareCards(playerHand, houseHand)
                            else:
                                userInput = input("Invalid")
                    case "d":
                        print("Doubling down")
                        money -= bet
                        bet += bet
                        print("You have", money, "dollars remaining")
                        playerHand.append(deck[0:1])
                        deck.extend(deck[0:1])
                        deck = deck[1:len(deck)]
                        dealerTurn(playerHand, houseHand)
                        cardsPlayed += 1
                        compareCards(playerHand, houseHand)
                    case "s":
                        print("Standing")
                        compareCards(playerHand, houseHand)
                    case "f":
                        print("Coward")
                        money += bet / 2
                        bet = 0
                        playing = False
                        break
            else:
                userInput = input("Invalid. Enter a, s, d, or f: ")
        if cardCheck(playerHand) == 21:
            print("Blackjack!")
            money += bet * 2.5
            playing = False
        elif cardCheck(playerHand) > 21:
            print("Bust! :(")
            bet = 0
            playing = False
        if cardsPlayed >= int(float(len(deck)) * percentDeckShuffle):
            shuffle()
            print("shuffling")

def startGame():  # starts the game
    print("Starting the game! Dealer stands on 17 or higher. Blackjack pays 1.5x")
    userInput = input("Enter starting money: ")
    global money
    money = int(userInput)

def displayHands(phand, dhand):  # displays hand info
    displayPlayerHand = str(phand)
    displayHouseHand = str(dhand[0])
    print("Your hand is ", displayPlayerHand[1:len(displayPlayerHand) - 1])
    print("Your total:", cardCheck(phand))
    sys.stdout.write('The house hand is ' + displayHouseHand + ', ?\n')

def cardCheck(hand):
    testHand = hand
    while testHand.count(11) > 0:
        b = testHand.index(11)
        testHand.insert(b, 10)
        testHand.pop(b + 1)
    while testHand.count(12) > 0:
        n = testHand.index(12)
        testHand.insert(n, 10)
        testHand.pop(n + 1)
    if sum(testHand) > 21 and testHand.count(13) > 0:
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

def dealerTurn(phand, dhand):
    global deck
    while cardCheck(dhand)<17:
        dhand.append(sum(deck[0:1]))
        deck.extend(deck[0:1])
        deck = deck[1:len(deck)]
    displayHands(phand, dhand)

bet = 0
money = 0
playing = True
cardsPlayed = 0
percentDeckShuffle = 0
userInput = input("Enter amount of decks: ")
amountDecks = int(userInput)
while True:
    userInput = input("Enter percent to shuffle deck at in decimal form: ")
    percentDeckShuffle = float(userInput)
    if percentDeckShuffle < .2:
        userInput = input("Enter percentage(>=.2) to shuffle deck at in decimal form: ")
        percentDeckShuffle = float(userInput)
        print("Must be .2 or greater")
    elif percentDeckShuffle >= .2:
        break
deck = list(range(1, 14)) * (amountDecks * 4)
shuffle()
startGame()
while money > 0 or playing:
    playHand()
print("You went bankrupt :(")
