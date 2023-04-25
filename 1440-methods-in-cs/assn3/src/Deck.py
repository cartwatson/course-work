import sys

from Card import Card
from NumberSet import NumberSet


class Deck():
    def __init__(self, cardSize, cardCount, numberMax):
        """Deck constructor"""
        self._cardCount = cardCount
        self._cardSize = cardSize
        self._numberMax = numberMax
        self._cards = []
        # create deck of cards
        for i in range(self._cardCount):
            # create numberSet
            tempNumSet = NumberSet(self._numberMax)
            tempNumSet.randomize()
            # create card
            tempCard = Card(i, self._cardSize, tempNumSet)
            # add card to deck
            self._cards.append(tempCard)

    def getCardCount(self):
        """Return an integer: the number of cards in this deck"""
        return self._cardCount

    def getCard(self, n):
        """Return card N from the deck"""
        card = None
        n -= 1
        if 0 <= n < self.getCardCount():
            card = self._cards[n]
        return card

    def print(self, file=sys.stdout, idx=None):
        """void function: Print cards from the Deck

        If an index is given, print only that card.
        Otherwise, print each card in the Deck
        """
        if idx is None:
            for idx in range(1, self._cardCount + 1):
                c = self.getCard(idx)
                c.print(file)
            print('', file=file)
        else:
            self.getCard(idx).print(file)

    def getCards(self, index=None):
        if index == None:
            return self._cards
        else:
            return self._cards[index]
