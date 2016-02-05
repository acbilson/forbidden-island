import unittest
import sys
sys.path.append('..\src')
from playerfactory import *
from constants import *

class TestPlayerFactory(unittest.TestCase):
  
    def test_ctor(self):
      factory = PlayerFactory()
