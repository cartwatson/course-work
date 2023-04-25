# Tests the Deck Class

import unittest
import Deck


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck.Deck(cardSize=7, cardCount=3, numberMax=100)
        self.deck1 = Deck.Deck(0, 0, 0)

    def test_getCardCount(self):
        self.assertNotEqual(self.deck.getCardCount(), 0)
        self.assertEqual(self.deck.getCardCount(), 3)
        self.assertEqual(self.deck1.getCardCount(), 0)

    def test_getCard(self):
        self.assertIsNotNone(self.deck.getCard(1))
        self.assertIsNone(self.deck.getCard(0))
        self.assertIsNone(self.deck1.getCard(1))

        # This requires the students to name their card array __m_cards.
        # .. It also accesses a private member which may not be preferred.
        self.assertIs(self.deck.getCards(0), self.deck.getCard(1))
        self.assertIs(self.deck.getCards(1), self.deck.getCard(2))
        self.assertIs(self.deck.getCards(2), self.deck.getCard(3))
        self.assertIsNot(self.deck.getCards(0), self.deck.getCard(2))
        self.assertIsNot(self.deck.getCards(1), self.deck.getCard(3))
        self.assertIsNot(self.deck.getCards(2), self.deck.getCard(1))


if __name__ == '__main__':
    unittest.main()
