import unittest
from constants import *
from player import *

class TestPlayer(unittest.TestCase):
  
    def test_ctor(self):
      player = Player(PlayerType.Diver)
