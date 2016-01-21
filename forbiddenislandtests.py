import unittest
from island import *
from tile import *
from islandnotifier import *
from constants import *
from islandmain import *
from player import *
from message import *

class TestIslandMessage(unittest.TestCase):

    def test_ctor(self):
      message = IslandMessage("test content", MessageType.Console)
      self.assertEqual("test content", message.content)
      self.assertEqual(MessageType.Console, message.type)

class TestConsoleMessage(unittest.TestCase):

    def test_ctor(self):
      message = ConsoleMessage("test content", MessageType.Console)
      self.assertEqual("test content", message.content)
      self.assertEqual(MessageType.Console, message.type)

class TestIslandGame(unittest.TestCase):

  def test_ctor(self):
    notifier = IslandNotifier()
    messageFactory = MessageFactory()
    main = IslandGame(notifier, messageFactory)

class TestPlayer(unittest.TestCase):
  
    def test_ctor(self):
      player = Player(PlayerType.Diver)

class TestIsland(unittest.TestCase):

  """ Testing the Island class """
  island = None

  def setUp(self):
    self.island = Island()

  def test_island_ctor(self):
    island = Island()

  def test_island_getBoard(self):
    self.assertEqual(TestConstants.EmptyBoard, self.island.board)

  def test_island_generateBoard(self):
    self.island.generateBoard()

  def test_island_getTile(self):
    self.island.board = TestConstants.GetTileBoard

    actual = self.island.getTile(TileName.CliffsOfAbandon)

    expected = Tile(index=494,
                    name=TileName.CliffsOfAbandon, 
                    player=PlayerType.Engineer, 
                    status=TileStatus.Sunken)

    self.assertEqual(expected.name, actual.name)

  def test_island_sinkTile(self):
    self.island.board = TestConstants.GetTileBoard

    self.island.sinkTile(TileName.CliffsOfAbandon)

    expected = TestConstants.SunkenBoard
    self.assertEqual(expected, self.island.board)

class TestTile(unittest.TestCase):

  """ Testing the Tile class """
  tile = None

  def setUp(self):
    self.tile = Tile(10, TileName.DunesOfDeception, PlayerType.Engineer, TileStatus.Raised)

  def test_tile_getIndices(self):
    actual = self.tile.getIndices()
    expected = (10, 10+39, 10+(39*2))

    self.assertEqual(expected, actual)

  def test_tile_getNameIndex(self):
    actual = self.tile.getNameIndex()

    self.assertEqual(10, actual)

class TestConstants():

  EmptyBoard = (
  '             /   \ /   \\              \n' + 
  '             |   | |   |              \n' +
  '             \   / \   /              \n' +
  '                                      \n' + 
  '      /   \ /   \ /   \ /   \\         \n' + 
  '      |   | |   | |   | |   |         \n' + 
  '      \   / \   / \   / \   /         \n' +
  '                                      \n' + 
  ' /   \ /   \ /   \ /   \ /   \ /   \\  \n' +
  ' |   | |   | |   | |   | |   | |   |  \n' +
  ' \   / \   / \   / \   / \   / \   /  \n' +
  '                                      \n' + 
  ' /   \ /   \ /   \ /   \ /   \ /   \\  \n' +
  ' |   | |   | |   | |   | |   | |   |  \n' +
  ' \   / \   / \   / \   / \   / \   /  \n' +
  '                                      \n' + 
  '       /   \ /   \ /   \ /   \\        \n' +
  '       |   | |   | |   | |   |        \n' +
  '       \   / \   / \   / \   /        \n' +
  '                                      \n' + 
  '             /   \ /   \\              \n' +
  '             |   | |   |              \n' +
  '             \   / \   /              \n')

  GetTileBoard = (
  '             /   \ /   \\              \n' + 
  '             |   | |   |              \n' +
  '             \   / \   /              \n' +
  '                                      \n' + 
  '      /   \ /   \ /   \ /   \\         \n' + 
  '      |   | |   | |   | |   |         \n' + 
  '      \   / \   / \   / \   /         \n' +
  '                                      \n' + 
  ' /   \ /   \ /   \ /   \ /   \ /   \\  \n' +
  ' |   | |   | |   | |   | |   | |   |  \n' +
  ' \   / \   / \   / \   / \   / \   /  \n' +
  '                                      \n' + 
  ' /   \ /   \ /   \ /   \ /COA\ /   \\  \n' +
  ' |   | |   | |   | |   | |ENG| |   |  \n' +
  ' \   / \   / \   / \   / \SNK/ \   /  \n' +
  '                                      \n' + 
  '       /   \ /   \ /   \ /   \\        \n' +
  '       |   | |   | |   | |   |        \n' +
  '       \   / \   / \   / \   /        \n' +
  '                                      \n' + 
  '             /   \ /   \\              \n' +
  '             |   | |   |              \n' +
  '             \   / \   /              \n')

  UpdateTileBoard = (
  '             /   \ /   \\              \n' + 
  '             |   | |   |              \n' +
  '             \   / \   /              \n' +
  '                                      \n' + 
  '      /   \ /   \ /   \ /   \\         \n' + 
  '      |   | |   | |   | |   |         \n' + 
  '      \   / \   / \   / \   /         \n' +
  '                                      \n' + 
  ' /   \ /   \ /   \ /   \ /   \ /   \\  \n' +
  ' |   | |   | |   | |   | |   | |   |  \n' +
  ' \   / \   / \   / \   / \   / \   /  \n' +
  '                                      \n' + 
  ' /   \ /   \ /   \ /   \ /DOD\ /   \\  \n' +
  ' |   | |   | |   | |   | |PLT| |   |  \n' +
  ' \   / \   / \   / \   / \   / \   /  \n' +
  '                                      \n' + 
  '       /   \ /   \ /   \ /   \\        \n' +
  '       |   | |   | |   | |   |        \n' +
  '       \   / \   / \   / \   /        \n' +
  '                                      \n' + 
  '             /   \ /   \\              \n' +
  '             |   | |   |              \n' +
  '             \   / \   /              \n')

  SunkenBoard = (
  '             /   \ /   \\              \n' + 
  '             |   | |   |              \n' +
  '             \   / \   /              \n' +
  '                                      \n' + 
  '      /   \ /   \ /   \ /   \\         \n' + 
  '      |   | |   | |   | |   |         \n' + 
  '      \   / \   / \   / \   /         \n' +
  '                                      \n' + 
  ' /   \ /   \ /   \ /   \ /   \ /   \\  \n' +
  ' |   | |   | |   | |   | |   | |   |  \n' +
  ' \   / \   / \   / \   / \   / \   /  \n' +
  '                                      \n' + 
  ' /   \ /   \ /   \ /   \       /   \\  \n' +
  ' |   | |   | |   | |   |       |   |  \n' +
  ' \   / \   / \   / \   /       \   /  \n' +
  '                                      \n' + 
  '       /   \ /   \ /   \ /   \\        \n' +
  '       |   | |   | |   | |   |        \n' +
  '       \   / \   / \   / \   /        \n' +
  '                                      \n' + 
  '             /   \ /   \\              \n' +
  '             |   | |   |              \n' +
  '             \   / \   /              \n')
