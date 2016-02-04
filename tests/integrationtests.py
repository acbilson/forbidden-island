import unittest
import sys
sys.path.append('..\src')
from islandgame import *
from consoleservice import *
from playerservice import *
from logservice import *
from screenservice import *
from iofactory import FakeIO

class TestGame(unittest.TestCase):

  def test_golden_initialization(self):

    """ When the game is initiated and the user enters valid input, should generate a board with all players """

    # Arrange
    bus = IslandBus()
    messageFactory = MessageFactory()
    game = IslandGame(bus, messageFactory)
    island = Island()
    pDeck = PlayerDeck()
    fio = FakeIO()

    fio.callStack = [StackItem(1, "What is your name? ", 'Alex\n' ),
                     StackItem(2, "How many players will be playing? ", '2\n' ),
                     StackItem(3, "Choose a player type: ", 'Diver\n' ),
                     StackItem(4, "Choose a player type: ", 'Engineer\n' )]

    cs = ConsoleService(bus, fio)
    ss = ScreenService(bus, island, fio)
    ps = PlayerService(bus, pDeck)
    ls = LogService(bus, fio)

    # Act
    game.play()

    board = island.getBoard()
    self.assertTrue (len(board) > 0)
    self.assertTrue(Constant.PlayerType["Diver"] in board)
    self.assertTrue(Constant.PlayerType["Engineer"] in board)
    
