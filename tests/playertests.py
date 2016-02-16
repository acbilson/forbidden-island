import unittest
import sys
sys.path.append('../src')
from player import *
from constants import *
from cards import *

class TestPlayer(unittest.TestCase):
  
  def test_ctor(self):

    p = Player(None)

    self.assertEqual(0, len(p.commandHistory))

  def test_move_whenATileIsSent_MovesPlayerLocationToThatTile(self):

    p = Player(None)

    p.move()
