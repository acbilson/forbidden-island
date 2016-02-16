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

class TestPlayerService(unittest.TestCase):

  ps = None

  def setUp(self):
    bus = IslandBus()
    playerFactory = PlayerFactory()
    self.ps = PlayerService(bus, playerFactory)

  def test_ctor(self):
    bus = IslandBus()
    playerFactory = PlayerFactory()
    ps = PlayerService(bus, playerFactory)

  def test_on_message_received_receivesCreateMessage_CreatesTwoPlayers(self):

    """ When a request for two players to be created is received, should add them to the player list """

    msg = PlayerMessage(Request(PlayerOptions.Create, [Constant.PlayerType["Diver"], Constant.PlayerType["Messenger"]]))

    self.ps.on_message_received(msg)

    self.assertEqual(2, len(self.ps.players))
  
  def test__get_screen_message_receivesTwoPlayers_returnsCreateMessage(self):

    commands = {'move': MoveCommand(PlayerMover)}
    players = [DiverPlayer(commands), PilotPlayer(commands)]

    actual = self.ps._get_screen_message(players)

    diverExpected = (Constant.PlayerType["Diver"], Constant.TileNames['IronGate'])
    pilotExpected = (Constant.PlayerType["Pilot"], Constant.TileNames['FoolsLanding'])

    self.assertEqual(diverExpected, actual.request.content[0])
    self.assertEqual(pilotExpected, actual.request.content[1])
