import unittest
from constants import *
from message import *

class TestIslandMessage(unittest.TestCase):

    def test_ctor(self):
      message = IslandMessage("test content", MessageType.All)
      self.assertEqual("test content", message.content)
      self.assertEqual(MessageType.All, message.type)

class TestBroadcastMessage(unittest.TestCase):

    def test_ctor(self):
      message = BroadcastMessage("Test broadcast")
      self.assertEqual("Test broadcast", message.content)
      self.assertEqual(MessageType.All, message.type)

class TestMoveMessage(unittest.TestCase):

    def test_ctor(self):
      message = MoveMessage("Up")
      self.assertEqual("Up", message.content)
      self.assertEqual(MessageType.Console_Move, message.type)
