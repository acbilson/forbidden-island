import unittest
import sys
sys.path.append('..\src')
from island import *
from islandbus import *
from islandservice import *
from playerservice import *
from constants import *
from message import *
from cards import *
import sys
sys.path.append('C:\SourceCode\PersonalRepo\Python\PyLexLib')
from iofactory import *

class TestPlayerService(unittest.TestCase):

  ps = None

  def setUp(self):
    bus = IslandBus()
    deck = PlayerDeck()
    self.ps = PlayerService(bus, deck)

  def test_ctor(self):
    bus = IslandBus()
    deck = PlayerDeck()
    ps = PlayerService(bus, deck)

  def test_on_message_received_receivesCreateMessage_CreatesTwoPlayers(self):

    """ When a request for two players to be created is received, should add them to the player list """

    msg = PlayerMessage(Request(PlayerOptions.Create, [Constant.PlayerType["Diver"], Constant.PlayerType["Messenger"]]))

    self.ps.on_message_received(msg)

    self.assertEqual(2, len(self.ps.players))
  
  def test__get_screen_message_receivesTwoPlayers_returnsCreateMessage(self):

    players = [Player(Constant.PlayerType["Diver"]), Player(Constant.PlayerType["Pilot"])]

    actual = self.ps._get_screen_message(players)

    diverExpected = (Constant.PlayerType["Diver"], Constant.TileNames['IronGate'])
    pilotExpected = (Constant.PlayerType["Pilot"], Constant.TileNames['FoolsLanding'])

    self.assertEqual(diverExpected, actual.request.content[0])
    self.assertEqual(pilotExpected, actual.request.content[1])
