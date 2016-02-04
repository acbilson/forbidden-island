from enum import Enum

class CardDeck(object):

  def __init__(self):
    self.cards = []

  def shuffle(self, cards):
    """ Shuffles a segment of cards """
    pass

  def getCard(self):
    """ Gets the top card from the deck """
    pass

class PlayerDeck(CardDeck):

  def __init__(self):
    pass

class IslandDeck(CardDeck):

  def __init__(self):
    pass


