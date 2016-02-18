import unittest
import sys
sys.path.append('../src')
from islandgame import *
from service_console import *
from service_player import *
from service_log import *
from service_screen import *
from iofactory import FakeIO
from tiles import *

class TestGame(unittest.TestCase):

  def test_golden_initialization(self):

    """ When the game is initiated and the user enters valid input, should generate a board with all players """

    # Arrange
    bus = IslandBus()
    messageFactory = MessageFactory()
    playerFactory = PlayerFactory()
    game = IslandGame(bus, messageFactory)
    island = Island()
    pDeck = PlayerDeck()
    fio = FakeIO()
    tiles = Tiles()

    fio.callStack = [StackItem(1, "What is your name? ", 'Alex\n' ),
                     StackItem(2, "How many players will be playing? ", '2\n' ),
                     StackItem(3, "Choose a player type: ", 'Diver\n' ),
                     StackItem(4, "Choose a player type: ", 'Engineer\n' )]

    cs = ConsoleService(bus, fio)
    ss = ScreenService(bus, island, fio, tiles)
    ps = PlayerService(bus, playerFactory, tiles)
    ls = LogService(bus, fio)

    # Act
    game.play()

    board = island.generate_board(tiles.tiles)
    self.assertTrue (len(board) > 0)
    self.assertTrue(Constant.PlayerType["Diver"] in board)
    self.assertTrue(Constant.PlayerType["Engineer"] in board)
