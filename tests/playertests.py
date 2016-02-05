import unittest
import sys
sys.path.append('..\src')
from player import *
from constants import *
from cards import *

class TestPlayer(unittest.TestCase):
  
  def test_ctor(self):

    commands = {'move': MoveCommand(PlayerMover())}
    p = Player(commands)

    self.assertTrue(len(p.commands) > 0)

  def test_move_whenATileIsSent_MovesPlayerLocationToThatTile(self):

    commands = {'move': MoveCommand(PlayerMover())}
    p = Player(commands)

    p.move()
