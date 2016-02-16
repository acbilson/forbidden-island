import unittest
import sys
sys.path.append('../src')
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

    """ When the island is retrieved, should already have been generated. """

    actual = self.island.getBoard()
      
    self.assertTrue(len(actual) > 0)

  def test_island_generateBoard_willNotDuplicate(self):

    """ When a board is generated a second time, should not append to previous board """

    originalLength = len(self.island.getBoard())

    # already run once at instantiation
    self.island.generateBoard()

    afterLength = len(self.island.getBoard())

    self.assertEqual(originalLength, afterLength)

  def test_island_getTile_afterTilesAreGenerated(self):

    """ When the board has been generated (at init), I should be able to retrieve a tile. """

    actual = self.island.getTile(Constant.TileNames["CliffsOfAbandon"])

    self.assertEqual("COA", actual.name.value)

  def test_island_updateTile(self):

    """ When I update a tile, should be reflected on the board. """

    updatedTile = Tile(index=494,
                       name=Constant.TileNames["DunesOfDeception"], 
                       player=Constant.PlayerType["Pilot"], 
                       status=Constant.TileStatus["Sunken"])

    self.island.updateTile(updatedTile)
    board = self.island.getBoard()

    self.assertTrue(Constant.PlayerType["Pilot"] in board)
    self.assertTrue(Constant.TileStatus["Sunken"] in board)

  def test_island_sinkTile(self):

    """ When I sink a tile, it should no longer be on the board. """

    tileToSink = self.island.getTile(Constant.TileNames["CliffsOfAbandon"])

    self.island.sinkTile(tileToSink)
    board = self.island.getBoard()

    self.assertFalse(Constant.TileNames["CliffsOfAbandon"] in board)

  def test__get_random_tiles(self):

    """ Should return six random tiles """

    first = self.island._get_random_tiles()
    second = self.island._get_random_tiles()

    self.assertEqual(6, len(first)) 
    self.assertTrue(first != second)

  def test_sink_first_tiles_success(self):

    self.island.sink_first_tiles()
    
    self.assertTrue(Constant.TileStatus["Sunken"] in self.island.getBoard())

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
