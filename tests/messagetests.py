import unittest
import sys
sys.path.append('..\src')
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
