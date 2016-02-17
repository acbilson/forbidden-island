import unittest
import sys
sys.path.append('../src')
from island import *
from service_island import *
from service_player import *
from islandbus import *
from constants import *
from message import *
from cards import *
import sys
from iofactory import *
from playerfactory import *
from tiles import *

class TestPlayerService(unittest.TestCase):

  ps = None

  def setUp(self):
    bus = IslandBus()
    playerFactory = PlayerFactory()
    tiles = Tiles()
    self.ps = PlayerService(bus, playerFactory, tiles)

  def test_ctor(self):
    bus = IslandBus()
    playerFactory = PlayerFactory()
    tiles = Tiles()
    ps = PlayerService(bus, playerFactory, tiles)

  def test_on_message_received_receivesCreateMessage_CreatesTwoPlayers(self):

    """ When a request for two players to be created is received, should add them to the player list """

    msg = PlayerMessage(Request(PlayerOptions.Create, [Constant.PlayerType["Diver"], Constant.PlayerType["Messenger"]]))

    self.ps.on_message_received(msg)

    self.assertEqual(2, len(self.ps.players))
 
  def test_on_message_received_receivesCreateMessage_updatesTiles(self):

    """ When a request for two players to be created is received, should add them to the tiles """

    msg = PlayerMessage(Request(PlayerOptions.Create, [Constant.PlayerType["Diver"]]))

    self.ps.on_message_received(msg)
    diverTile = self.ps.tiles.get_tile(Constant.TileNames["IronGate"])

    self.assertEqual(Constant.PlayerType["Diver"], diverTile.player.value)
