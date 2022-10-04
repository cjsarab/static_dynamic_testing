import unittest
from src.card import Card
from src.card_game import *

class TestCard (unittest.TestCase):

    def setUp(self):
        self.card1 = Card("Hearts", 1)
        self.card2 = Card("Spades", 6)
        self.cardgame = CardGame()

    def test_check_for_ace(self):
        card = self.card1
        results = self.cardgame.check_for_ace(card)
        self.assertEqual(True, results)

    def test_highest_card(self):
        results = self.cardgame.highest_card(self.card1, self.card2)
        self.assertEqual(self.card2, results)

    def test_cards_total(self):
        cards = [self.card1, self.card2]
        results = self.cardgame.cards_total(cards)
        self.assertEqual("You have a total of 7", results)
