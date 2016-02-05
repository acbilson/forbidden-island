import unittest
import sys
sys.path.append('..\src')
from island import *
from islandbus import *
from service_island import *
from service_screen import *
from constants import *
from message import *
from cards import *
import sys
sys.path.append('C:\SourceCode\PersonalRepo\Python\PyLexLib')
from iofactory import *

class TestScreenService(unittest.TestCase):

  ss = None
  fio = None

  def setUp(self):
    bus = IslandBus()
    island = Island()
    self.fio = FakeIO()
    self.ss = ScreenService(bus, island, self.fio)

  def test_ctor(self):
    bus = IslandBus()
    island = Island()
    fio = FakeIO()
    ss = ScreenService(bus, island, fio)

  def test_on_message_received_emptyMessage_nothingHappens(self):

    """ When a message is received, if it is not handled by this service, None is returned """

    msg = ScreenMessage(Request(""))
    actual = self.ss.on_message_received(msg)

    self.assertIsNone(actual)

  def test_on_message_received_render_printsBoard(self):

    """ When a render message is received, the board is rendered """

    msg = ScreenMessage(Request(ScreenOptions.Render))

    self.ss.on_message_received(msg)

    # Something was rendered
    self.assertTrue(len(self.fio.writeContent) > 0)

  def test_on_message_received_addPlayers_areAdded(self):

    """ When a request to add two players to the board is received, the island is updated with the requested players """
    self.ss.island.generateBoard()

    playerTuple = (Constant.PlayerType["Explorer"], Constant.TileNames["CopperGate"]), (Constant.PlayerType["Messenger"],
    Constant.TileNames["SilverGate"])
    msg = ScreenMessage(Request(ScreenOptions.AddPlayers, playerTuple))

    self.ss.on_message_received(msg)

    self.assertTrue(Constant.PlayerType["Explorer"] in self.ss.island.getBoard())
    self.assertTrue(Constant.PlayerType["Messenger"] in self.ss.island.getBoard())

# Message for these tests
class TestMessage(IslandMessage):

  def __init__(self, request):
    IslandMessage.__init__(self, MessageType.Test, request)
