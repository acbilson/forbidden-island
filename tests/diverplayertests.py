import unittest
import sys
sys.path.append('..\src')
from diverplayer import *
from constants import *

class TestDiverPlayer(unittest.TestCase):
  
    def test_ctor(self):
      diver = DiverPlayer()

      self.assertTrue(len(diver.commands) > 0)
      self.assertEqual(Constant.TileNames["IronGate"], diver.currentLocation)
