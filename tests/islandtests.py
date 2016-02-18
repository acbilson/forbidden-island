import unittest
import sys
sys.path.append('../src')
from island import *
from tile import *
from player import *
from constants import *
from tiles import *

class TestIsland(unittest.TestCase):

  """ Testing the Island class """

  island = None

  def setUp(self):
    self.island = Island()

  def test_island_ctor(self):
    island = Island()

  def test_island_generate_board_returnsBoard(self):

    """ When the island is generated, should return a board. """
  
    # Generate tiles
    t = Tiles()
    testTiles = []
    for i in range(0,23):
      testTiles.append(Tile(i, "TST", "   ", "   "))
    t.tiles = testTiles

    actual = self.island.generate_board(t.tiles)
      
    self.assertTrue(len(actual) > 0)

class TestTile(unittest.TestCase):

  """ Testing the Tile class """

  tile = None

  def setUp(self):
    self.tile = Tile(10, Constant.TileNames["DunesOfDeception"], Constant.PlayerType["Engineer"],
    Constant.TileStatus["Raised"])

  def test_tile_getIndices(self):
    actual = self.tile.getIndices()
    expected = (10, 10+39, 10+(39*2))

    self.assertEqual(expected, actual)

  def test_tile__getNameIndex(self):
    actual = self.tile.getNameIndex()

    self.assertEqual(10, actual)

  def test_tile_sink_updatesValue(self):

    """ When a tile is sunk, should have empty name, player and status """

    self.tile.sink()
    
    self.assertEqual("     ", self.tile.name.value)
    self.assertEqual("     ", self.tile.player.value)
    self.assertEqual("     ", self.tile.status.value)

  def test_tile_sink_updatesIndex(self):

    """ When a tile is sunk, should have a different index to reflect the missing side markers """

    ni = self.tile.name.index
    pi = self.tile.player.index
    si = self.tile.status.index
    self.tile.sink()
    
    self.assertEqual(ni - 1, self.tile.name.index)
    self.assertEqual(pi - 1, self.tile.player.index)
    self.assertEqual(si - 1, self.tile.status.index)
