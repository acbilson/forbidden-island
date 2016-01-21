import unittest
from island import *
from tile import *
from islandbus import *
from islandservice import *
from constants import *
from islandgame import *
from player import *
from message import *

class TestIslandGame(unittest.TestCase):

  def test_ctor(self):
    bus = IslandBus()
    messageFactory = MessageFactory()
    main = IslandGame(bus, messageFactory)
    main.play()
