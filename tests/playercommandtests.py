import unittest
import sys
sys.path.append('..\src')
from constants import *
from playercommand import *
from island import *

class TestPlayerInvoker(unittest.TestCase):

  pi = None

  def setUp(self):

    mover = PlayerMover()
    moveCommand = MoveCommand(mover)
    commands = {'move': moveCommand}
    self.pi = PlayerInvoker(commands)

  def test_ctor(self):
    
    mover = PlayerReceiver()
    moveCommand = MoveCommand(mover)
    commands = {'move': moveCommand}
    self.pi = PlayerInvoker(commands)

  def test_move_works(self):

    self.pi.move()

class TestMoveCommand(unittest.TestCase):

  def test_ctor(self):

    mover = PlayerMover()
    mc = MoveCommand(mover)

  def test_execute(self):
    pass

