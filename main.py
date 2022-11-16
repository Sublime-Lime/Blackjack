import random


class blackjack:
    def __init__(self, deck, initialFunds, playerCount, percentage):
        self.deck = list(range(2, 14)) * (int(deck) * 4)
        self.money = initialFunds
        self.count = playerCount
        self.percentage = percentage
        self.state = True
        self.cardsPlayed = 0
        self.bet = 0

    def dealCards(self):
        self.playerHand = self.deck[0:2]
        self.houseHand = self.deck[2:4]
        self.deck.extend(self.deck[0:4])
        self.deck = self.deck[4:len(self.deck)]
        self.cardsPlayed += 4

    def printMoney(self):
        print("You have: " + str(self.money) + " $$$$$$$")

    def getBet(self):
        self.printMoney()
        while True:
            userInput = input("Enter bet: ")
            self.bet = int(userInput)
            if self.bet <= self.money:
                self.money -= self.bet
                break
            print("you poor shut up")

        self.printMoney()

    def printHand(self):
        print("Your hand is ", str(self.playerHand)[1:len(str(self.playerHand)) - 1])
        print("Your total:", self.cardCheck(self.playerHand))
        print("The house hand is", str(self.houseHand[0]), "+ ?")

    def dealerTurn(self):
        while self.cardCheck(self.houseHand) < 17:
            self.houseHand.append(sum(self.deck[0:1]))
            self.deck.extend(self.deck[0:1])
            self.deck = self.deck[1:len(self.deck)]
        print("The dealers hand is", self.houseHand[1:len(self.houseHand) - 1])

    def shuffleDeck(self):
        random.shuffle(self.deck)
        print("shuffling")

    def cardCheck(self, hand):
        testHand = hand
        while testHand.count(11) > 0:
            n = testHand.index(11)
            testHand.insert(n, 10)
            testHand.pop(n + 1)
        while testHand.count(12) > 0:
            n = testHand.index(12)
            testHand.insert(n, 10)
            testHand.pop(n + 1)
        while testHand.count(13) > 0:
            n = testHand.index(13)
            testHand.insert(n, 10)
            testHand.pop(n + 1)
        if sum(testHand) > 21 and testHand.count(14) > 0:
            while testHand.count(13) > 0:
                n = testHand.index(13)
                testHand.insert(n, 1)
                testHand.pop(n + 1)
            return sum(testHand)
        elif testHand.count(14) > 0:
            while testHand.count(14) > 0:
                n = testHand.index(14)
                testHand.insert(n, 11)
                testHand.pop(n + 1)
            return sum(testHand)
        else:
            return sum(testHand)

    def compareCards(self):
        if self.cardCheck(self.playerHand) > self.cardCheck(self.houseHand):
            self.money += self.bet * 2
            print("You won!!!")
            self.state = False
        elif self.cardCheck(self.playerHand) == self.cardCheck(self.houseHand):
            print("You drew")
            self.money += self.bet
            self.state = False
        else:
            print("You lost")
            self.bet = 0
            self.state = False

    def naturalCheckDealer(self):
        if self.cardCheck(self.houseHand) == 21:
            print("Dealer has blackjack. You lose")
            self.bet = 0
            self.state = False

    def playHand(self):  # plays a round of blackjack
        state = True
        # print("shuffling every", int(float(len(deck)) * percentDeckShuffle), "cards")
        while state:
            print("You have", self.money, "dollars remaining")
            # Player Actions
            self.printMoney()
            self.naturalCheckDealer()
            if self.cardCheck(self.playerHand) == 21:
                print("self!")
                self.money += self.bet * 2.5
                self.state = False
            while self.cardCheck(self.playerHand) < 21 and self.state:
                print("hit(a), stand(s), double down(d), or surrender(f)")
                print(self.cardsPlayed, "cards played")
                userInput = input("Enter a, d, or s: ")
                if userInput == "a" or userInput == "s" or userInput == "d" or userInput == "f":
                    match userInput:
                        case "a":
                            print("Adding card")
                            self.cardsPlayed += 1
                            self.playerHand.append(sum(self.deck[0:1]))
                            self.deck.extend(self.deck[0:1])
                            self.deck = self.deck[1:len(self.deck)]
                            self.printMoney()
                            self.cardsPlayed += 1

                            while self.cardCheck(self.playerHand) < 21 and self.state:
                                print("hit(a) or stand(s)")
                                userInput = input("Enter a or s: ")
                                if self.cardCheck(self.playerHand) == 21:
                                    print("self!")
                                    self.money += self.bet * 2.5
                                    self.state = False
                                if userInput == "a":
                                    self.playerHand.append(sum(self.deck[0:1]))
                                    self.deck.extend(self.deck[0:1])
                                    self.decks = self.deck[1:len(self.deck)]
                                    self.printMoney()
                                    self.cardsPlayed += 1
                                elif userInput == "s":
                                    self.dealerTurn()
                                    self.compareCards()
                                else:
                                    userInput = input("Invalid. Enter correct response: ")
                        case "d":
                            print("Doubling down")
                            if self.money < self.bet:
                                print("You are broke and cannot bet anymore. Cancelling bet")
                                print("hit(a) or stand(s)")
                                userInput = input("Enter a or s: ")
                                if self.cardCheck(self.playerHand) == 21:
                                    print("self!")
                                    self.money += self.bet * 2.5
                                    self.state = False
                                if userInput == "a":
                                    self.playerHand.append(sum(self.deck[0:1]))
                                    self.deck.extend(self.deck[0:1])
                                    self.deck = self.deck[1:len(self.deck)]
                                    self.printMoney()
                                    self.cardsPlayed += 1
                                elif userInput == "s":
                                    self.dealerTurn()
                                    self.compareCards()
                                else:
                                    userInput = input("Invalid")
                            else:
                                self.money -= self.bet
                                self.bet += self.bet
                                print("You have", self.money, "dollars remaining")
                                self.playerHand.append(self.deck[0:1])
                                self.deck.extend(self.deck[0:1])
                                self.deck = self.deck[1:len(self.deck)]
                                self.dealerTurn()
                                self.cardsPlayed += 1
                                self.compareCards()
                        case "s":
                            print("Standing")
                            self.dealerTurn()
                            self.compareCards()
                        case "f":
                            print("Coward")
                            self.money += self.bet / 2
                            self.bet = 0
                            self.state = False
                            break
                else:
                    userInput = input("Invalid. Enter a, s, d, or f: ")
            if self.cardCheck(self.playerHand) > 21:
                print("Bust! :(")
                self.bet = 0
                self.state = False
            if self.cardsPlayed >= int(float(len(self.deck)) * self.percentage):
                self.shuffleDeck()
                print("shuffling")


class AIPlayer:
    AIHand = []

    def __init__(self, name):
        self.name = name

    def AIhanddeal(self):
        AIHand = blackjack.deck[0:2]
        blackjack.deck.extend(blackjack.deck[0:2])
        blackjack.deck = blackjack.deck[2:len(blackjack.deck)]
        displayAIHand = str(AIHand)
        print(self.name, "has the hand", displayAIHand[1:len(displayAIHand) - 1])


if __name__ == '__main__':
    userInput = input("How many decks do you want to play: ")
    deck = int(userInput)
    userInput = input("How rich you: ")
    money = int(userInput)
    names = []
    with open('names.txt', encoding='utf-8') as f:  # inputs names from names.txt into list
        for x in range(18000):
            names.append(f.readline().strip('\n'))
    while True:  # generates AI players
        userInput = input("Input number of AI players: ")
        count = int(userInput)
        if count < 0:
            print("Player count cannot be lower than 0")
            userInput = input("Input number of AI players: ")
            count = int(userInput)
        else:
            playerNamesNum = []
            for x in range(count):
                print(names[x], "is playing")
                playerNamesNum.append('player' + str(x))
                playerNamesNum[x] = AIPlayer(names[x])
        break
    while True:
        userInput = input("How much you wanna reshuffle: ")
        percentage = float(userInput)
        if percentage < .2:
            userInput = input("Enter percentage(>=.2) to shuffle deck at in decimal form: ")
            percentage = float(userInput)
            print("Must be .2 or greater")
        elif percentage >= .2:
            break

    blackjack = blackjack(deck, money, count, percentage)

    print("Starting the game! Dealer stands on 17 or higher. blackjack pays 1.5x")
    while blackjack.money > 0 or blackjack.state:
        blackjack.dealCards()
        blackjack.getBet()
        blackjack.printHand()
        if len(playerNamesNum) > 0:
            for x in range(count):
                playerNamesNum[x].AIhanddeal()
        blackjack.playHand()
