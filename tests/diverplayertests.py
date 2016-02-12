import unittest
import sys
sys.path.append('..\src')
from player_diver import *
from constants import *

class TestDiverPlayer(unittest.TestCase):
  
    def test_ctor(self):
      commands = {'move': MoveCommand(PlayerMover)}
      diver = DiverPlayer(commands)

      self.assertEqual(Constant.TileNames["IronGate"], diver.currentLocation)
