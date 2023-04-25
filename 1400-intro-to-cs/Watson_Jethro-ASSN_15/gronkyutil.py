import random

paw = ["Rock", "Paper", "Scissors"]
coin = ["Heads", "Tails"]
maxCardValue = 20


# Make sure you understand this to do the opposite conversion!!!
def convertCardToValue(cardValue, cardPaw, cardCoin):
    return 2 * ((cardValue - 1) + (maxCardValue * paw.index(cardPaw))) + coin.index(cardCoin)


def convertIDToCard(val):
    coin_index = abs(val % 2)
    val //= 2
    paw_index = abs(val // 20)
    val -= paw_index * 20
    return val + 1, paw[paw_index], coin[coin_index]


class card:
    def __init__(self, num):
        self.__list = []
        self.__list = convertIDToCard(num)
        self.__value = self.__list[0]
        self.__paw = self.__list[1]
        self.__coin = self.__list[2]
        self.__id = convertCardToValue(self.__value, self.__paw, self.__coin)

    def getID(self):
        return self.__id

    def getPaw(self):
        return self.__paw

    def getCoin(self):
        return self.__coin

    def getValue(self):
        return self.__value


class deck:
    def __init__(self):
        self.__internal_deck = []
        self.__internal_deck = self.generate_deck()
        self.__id = 0

    def shuffle(self):
        self.__internal_deck = self.generate_deck()
        random.shuffle(self.__internal_deck)

    def draw(self):
        return self.__internal_deck.pop()

    def generate_deck(self):
        self.__internal_deck.clear()
        # value
        for valStatus in range(maxCardValue):
            # paw
            for pawStatus in paw:
                # coin
                for coinStatus in coin:
                    self.__id = convertCardToValue(valStatus+1, pawStatus, coinStatus)
                    self.__internal_deck.append(card(self.__id))
        return self.__internal_deck
