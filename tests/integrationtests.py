import unittest
import sys
sys.path.append('..\src')
from islandgame import *
from iofactory import FakeIO

class TestGame(unittest.TestCase):

  def test_golden_initialization(self):

    """ When the game is initiated and the user enters valid input, should complete without error """

    # Arrange
    bus = IslandBus()
    messageFactory = MessageFactory()
    game = IslandGame(bus, messageFactory)
    fio = FakeIO()

    fio.callStack = [StackItem(1, "What is your name? ", 'Alex\n' ),
                     StackItem(2, "How many players will be playing? ", '1\n' ),
                     StackItem(3, "Choose a player type: ", 'Diver\n' )]

    cs = ConsoleService(bus, fio)
    ps = PlayerService(bus)
    ls = LogService(bus, fio)

    # Act
    game.play()

