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

class CardType(Enum):
  WatersRise = 1
  Sandbag = 2
  Airlift = 3
  Earth = 4
  Water = 5
  Air = 6
  Fire = 7


