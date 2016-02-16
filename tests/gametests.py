import unittest
import sys
sys.path.append('../src')
from island import *
from tile import *
from islandbus import *
from service_island import *
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
