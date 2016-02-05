import unittest
import sys
sys.path.append('..\src')
from player import *
from constants import *
from cards import *

class TestPlayer(unittest.TestCase):
  
  def test_ctor(self):

    p = Player(Constant.PlayerType["Diver"])

    self.assertTrue(len(p.commands) > 0)

  def test_get_start_location_pilot_foolslanding(self):

    """ When I retrieve the start location for a pilot, should return Fool's Landing """

    p = Player(Constant.PlayerType["Pilot"])
    
    actual = p.get_start_location()

    self.assertEqual(Constant.TileNames["FoolsLanding"], actual)

  def test_move_whenATileIsSent_MovesPlayerLocationToThatTile(self):

    p = Player(Constant.PlayerType["Pilot"])

    p.move()
