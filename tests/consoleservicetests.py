import unittest
import sys
sys.path.append('../src')
from island import *
from islandbus import *
from service_island import *
from service_console import *
from constants import *
from message import *
from cards import *
import sys
from iofactory import *

class TestConsoleService(unittest.TestCase):

  cs = None
  fio = None
  bus = None

  def setUp(self):
    self.bus = IslandBus()
    self.fio = FakeIO()
    self.cs = ConsoleService(self.bus, self.fio)

  def test_ctor(self):
    bus = IslandBus()
    fio = FakeIO()
    cs = ConsoleService(bus, fio)

  def test_on_message_received_notHandled(self):
    msg = ScreenMessage(Request("Test screen message"))
    self.cs.on_message_received(msg)

  def test_read_playertype_receivesCountOfTwo_returnsTwoMessages(self):

    """ When two player types are read, should send out a creation message with two player types """

    self.fio.callStack = [StackItem(1, "Choose a player type: ", 'Diver\n' ),
                          StackItem(2, "Choose a player type: ", 'Engineer\n' )]

    actual = self.cs.read_playertype(2)

    expected = [Constant.PlayerType["Diver"], Constant.PlayerType["Engineer"]]
    self.assertEqual(expected, actual.request.content)

  # TODO: Figure out what this is going to do
  def test_start_next_receivesUserInput_returns(self):

    self.cs.next(None)

# Message for these tests
class TestMessage(IslandMessage):

  def __init__(self, request):
    IslandMessage.__init__(self, MessageType.Test, request)
