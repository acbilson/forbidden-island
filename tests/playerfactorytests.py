import unittest
import sys
sys.path.append('..\src')
from playerfactory import *
from constants import *

class TestPlayerFactory(unittest.TestCase):

  factory = None

  def setUp(self):
    self.factory = PlayerFactory()


  def test_ctor(self):
    factory = PlayerFactory()

  def test_get_instance_diver(self):
    diver = self.factory.get_instance(Constant.PlayerType["Diver"])

  def test_get_instance_explorer(self):
    diver = self.factory.get_instance(Constant.PlayerType["Explorer"])

  def test_get_instance_navigator(self):
    diver = self.factory.get_instance(Constant.PlayerType["Navigator"])

  def test_get_instance_messenger(self):
    diver = self.factory.get_instance(Constant.PlayerType["Messenger"])

  def test_get_instance_pilot(self):
    diver = self.factory.get_instance(Constant.PlayerType["Pilot"])

  def test_get_instance_engineer(self):
    diver = self.factory.get_instance(Constant.PlayerType["Engineer"])
