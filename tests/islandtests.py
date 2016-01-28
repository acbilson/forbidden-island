import unittest
import sys
sys.path.append('..\src')
from island import *
from tile import *
from player import *
from constants import *

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
    # print('\n' + self.island.board)

  def test_island_getTile(self):
    self.island.board = TestConstants.GetTileBoard

    actual = self.island.getTile(TileName.CliffsOfAbandon)

    expected = Tile(index=494,
                    name=TileName.CliffsOfAbandon, 
                    player=PlayerType.Engineer, 
                    status=TileStatus.Sunken)

    self.assertEqual(expected.name, actual.name)

  def test_island_updateTile(self):
    self.island.board = TestConstants.GetTileBoard

    updatedTile = Tile(index=494,
                       name=TileName.DunesOfDeception, 
                       player=PlayerType.Pilot, 
                       status=TileStatus.Raised)

    self.island.updateTile(updatedTile)

    expected = TestConstants.UpdateTileBoard
    actual = self.island.board
    self.assertEqual(expected, actual)



  def test_island_sinkTile(self):
    self.island.board = TestConstants.GetTileBoard

    tileToSink = Tile(index=494,
                      name=TileName.CliffsOfAbandon, 
                      player=PlayerType.Engineer, 
                      status=TileStatus.Sunken)

    self.island.sinkTile(tileToSink)

    expected = TestConstants.SunkenBoard
    actual = self.island.board
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

  def test_tile_sink_updatesValue(self):
    self.tile.sink()
    
    self.assertEqual("     ", self.tile.name.value)
    self.assertEqual("     ", self.tile.player.value)
    self.assertEqual("     ", self.tile.status.value)

  def test_tile_sink_updatesIndex(self):
    ni = self.tile.name.index
    pi = self.tile.player.index
    si = self.tile.status.index
    self.tile.sink()
    
    self.assertEqual(ni - 1, self.tile.name.index)
    self.assertEqual(pi - 1, self.tile.player.index)
    self.assertEqual(si - 1, self.tile.status.index)


class TestConstants():

  EmptyBoard = (
  '             /   \ /   \\              \n' + 
  '             |   | |   |              \n' +
  '             \   / \   /              \n' +
  '                                      \n' + 
  '       /   \ /   \ /   \ /   \\        \n' + 
  '       |   | |   | |   | |   |        \n' + 
  '       \   / \   / \   / \   /        \n' +
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
  '       /   \ /   \ /   \ /   \\        \n' + 
  '       |   | |   | |   | |   |        \n' + 
  '       \   / \   / \   / \   /        \n' +
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
  '       /   \ /   \ /   \ /   \\        \n' + 
  '       |   | |   | |   | |   |        \n' + 
  '       \   / \   / \   / \   /        \n' +
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
  '       /   \ /   \ /   \ /   \\        \n' + 
  '       |   | |   | |   | |   |        \n' + 
  '       \   / \   / \   / \   /        \n' +
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
