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
from iofactory import *
from tiles import *

class TestScreenService(unittest.TestCase):

  ss = None
  fio = None

  def setUp(self):
    bus = IslandBus()
    island = Island()
    self.fio = FakeIO()
    tiles = Tiles()
    self.ss = ScreenService(bus, island, self.fio, tiles)

  def test_ctor(self):
    bus = IslandBus()
    island = Island()
    fio = FakeIO()
    tiles = Tiles()
    ss = ScreenService(bus, island, fio, tiles)

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

# Message for these tests
class TestMessage(IslandMessage):

  def __init__(self, request):
    IslandMessage.__init__(self, MessageType.Test, request)
