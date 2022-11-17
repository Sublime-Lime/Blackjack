import random
import pandas as pd


class blackjack:
    def __init__(self, deck, initialFunds, percentage):
        self.deck = list(range(2, 14)) * (int(deck) * 4)
        self.money = initialFunds
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
        print("The dealers hand is", str(self.houseHand)[1:len(str(self.houseHand)) - 1])
        print("The dealers total is", self.cardCheck(self.houseHand))

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
        if testHand.count(14) > 0 and sum(testHand) > 21:
            while testHand.count(14) > 0:
                n = testHand.index(14)
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
        if self.cardCheck(self.houseHand)>21:
            self.money += self.bet * 2
            print("Dealer bust. You won!!!")
            self.state = False
        elif self.cardCheck(self.playerHand) > self.cardCheck(self.houseHand):
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
        self.state = True
        # print("shuffling every", int(float(len(deck)) * percentDeckShuffle), "cards")

        while self.state and self.money > 0:
            self.getBet()
            self.dealCards()
            self.printHand()
            if len(playerNamesNum) > 0:
                for x in AIPlayer.registry:
                    x.AIhanddeal()
            self.naturalCheckDealer()
            if self.cardCheck(self.playerHand) == 21:
                print("blackjack!")
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
                            self.printHand()
                            while self.cardCheck(self.playerHand) < 21 and self.state:
                                print("hit(a) or stand(s)")
                                userInput = input("Enter a or s: ")
                                if self.cardCheck(self.playerHand) == 21:
                                    print("blackjack!")
                                    self.money += self.bet * 2.5
                                    self.state = False
                                    break
                                if userInput == "a":
                                    self.playerHand.append(sum(self.deck[0:1]))
                                    self.deck.extend(self.deck[0:1])
                                    self.deck = self.deck[1:len(self.deck)]
                                    self.printHand()
                                    self.cardsPlayed += 1
                                elif userInput == "s":
                                    for x in AIPlayer.registry:
                                        x.AITurn()
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
                                    print("blackjack!")
                                    self.money += self.bet * 2.5
                                    self.state = False
                                    break
                                if userInput == "a":
                                    self.playerHand.append(sum(self.deck[0:1]))
                                    self.deck.extend(self.deck[0:1])
                                    self.deck = self.deck[1:len(self.deck)]
                                    self.printHand()
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
                                self.playerHand.append(sum(self.deck[0:1]))
                                self.deck.extend(self.deck[0:1])
                                self.deck = self.deck[1:len(self.deck)]
                                self.printHand()
                                for x in AIPlayer.registry:
                                    x.AITurn()
                                self.dealerTurn()
                                self.cardsPlayed += 1
                                self.compareCards()
                        case "s":
                            print("Standing")
                            for x in AIPlayer.registry:
                                x.AITurn()
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
                for x in AIPlayer.registry:
                    x.AITurn()
                print("Bust! :(")
                self.bet = 0
                self.state = False
                break
            if self.cardsPlayed >= int(float(len(self.deck)) * self.percentage):
                self.shuffleDeck()
                print("shuffling")
            if self.cardCheck(self.playerHand) == 21:
                print("blackjack!")
                for x in AIPlayer.registry:
                    x.AITurn()
                self.money += self.bet * 2.5
                self.state = False
            if self.money > 0:
                self.state = True
            else:
                break

    def NPCintegration(self): # written inefficiently fix later
        NPCinfo = self.houseHand[0]
        if NPCinfo == 11:
            NPCinfo = 10
        if NPCinfo == 12:
            NPCinfo = 10
        if NPCinfo == 13:
            NPCinfo = 10
        if NPCinfo == 14:
            NPCinfo = 11
        return NPCinfo


class AIPlayer:
    AIHand = []
    registry = []

    def __init__(self, name):
        self.name = name
        # state of hard or soft hand. True = hard False = soft Get it?
        self.mohsScale = True
        self.displayAIHand = ""
        self.bet = 0
        self.money = blackjack.money
        self.registry.append(self)
        self.name = name

    def AIhanddeal(self):
        self.AIHand = blackjack.deck[0:2]
        blackjack.deck.extend(blackjack.deck[0:2])
        blackjack.deck = blackjack.deck[2:len(blackjack.deck)]
        self.displayAIHand = str(self.AIHand)
        print(self.name, "has the hand", self.displayAIHand[1:len(self.displayAIHand) - 1])
        blackjack.cardsPlayed += 1

    def cardCheck(self):
        testHand = self.AIHand
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
                self.mohsScale = False
            return sum(testHand)
        else:
            return sum(testHand)

    def AIBet(self):
        print(self.name, "has", self.money, "dollars")
        self.bet = ((random.randint(5, 10)/100) * self.money)
        print(self.name, "bet", self.bet)

    def compareAI(self):
        if self.cardCheck() > blackjack.cardCheck(blackjack.houseHand):
            self.money += self.bet * 2
            print(self.name, "won", self.bet)
        elif self.cardCheck() == blackjack.cardCheck(blackjack.houseHand):
            print(self.name, "drew")
            self.money += self.bet
        else:
            print(self.name, "lost", self.bet)
            self.bet = 0

    def AITurn(self):
        AIhard = pd.read_csv('npchard.csv')
        AIsoft = pd.read_csv('npcsoft.csv')
        AIpair = pd.read_csv('npcpair.csv')
        self.cardCheck()
        self.AIBet()
        while self.mohsScale:
            print(self.cardCheck(), str(blackjack.NPCintegration()))
            move = AIhard.loc[str(self.cardCheck()), str(blackjack.NPCintegration())]
            if move == "H":
                self.AIHand.append(blackjack.deck[0:1])
                blackjack.deck.extend(blackjack.deck[0:1])
                blackjack.deck = blackjack.deck[1:len(blackjack.deck)]
            elif move == "S":
                break
        while not self.mohsScale:
            move = AIsoft.loc[str(self.cardCheck()), str(blackjack.NPCintegration())]
            if move == "H":
                self.AIHand.append(blackjack.deck[0:1])
                blackjack.deck.extend(blackjack.deck[0:1])
                blackjack.deck = blackjack.deck[1:len(blackjack.deck)]
            elif move == "S":
                break
        self.displayAIHand = str(self.AIHand)
        print(self.name, "has the hand", self.displayAIHand[1:len(self.displayAIHand)-1])
        self.compareAI()


if __name__ == '__main__':
    userInput = input("How many decks do you want to play: ")
    deck = int(userInput)
    userInput = input("How rich you: ")
    money = int(userInput)
    while True:
        userInput = input("Percent in decimal to shuffle at: ")
        percentage = float(userInput)
        if percentage < .2:
            userInput = input("Enter percentage(>=.2) to shuffle deck at in decimal form: ")
            percentage = float(userInput)
            print("Must be .2 or greater")
        elif percentage >= .2:
            break

    blackjack = blackjack(deck, money, percentage)

    names = []
    with open('names.txt', encoding='utf-8') as f:  # inputs names from names.txt into list
        for x in range(18000):
            names.append(f.readline().strip('\n'))
    random.shuffle(names)
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
    print("Starting the game! Dealer stands on 17 or higher. blackjack pays 1.5x")
    blackjack.shuffleDeck()
    while blackjack.money > 0 or blackjack.state:
        blackjack.playHand()
    print("You went bankrupt :(")
