import unittest
import sys
sys.path.append('..\src')
from constants import *
from message import *

class TestIslandMessage(unittest.TestCase):

    def test_ctor(self):
      message = IslandMessage(MessageType.All, Request("test content"))
      self.assertIsNotNone(message.request)
      self.assertEqual(MessageType.All, message.type)
