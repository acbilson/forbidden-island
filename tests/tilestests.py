import unittest
import sys
sys.path.append('../src')
from tiles import *
from constants import *

class TestTiles(unittest.TestCase):
  
  tiles = None

  def setUp(self):
    self.tiles = Tiles()

  def test_ctor(self):
    t = Tiles()

    self.assertTrue(len(t.tiles) > 0)

  def test_get_tile_goodName_returnsTile(self):

    """ When a name is passed to get_tile, returns the correct Tile """

    actual = self.tiles.get_tile(Constant.TileNames["CliffsOfAbandon"])

    self.assertEqual(Constant.TileNames["CliffsOfAbandon"], actual.name.value)
  
  def test_sink_tile_goodName_sinksTile(self):

    """ When a tile is selected to be sunk, returns None """

    self.tiles.sink_tile(Constant.TileNames["DunesOfDeception"])
    
    tile = self.tiles.get_tile(Constant.TileNames["DunesOfDeception"])

    self.assertEqual(None, tile)

  def test_update_tile_goodTile_changesTile(self):

    """ When a tile is updates, should be reflected in the tiles list """

    tileToUpdate = Tile(999, Constant.TileNames["IronGate"], Constant.PlayerType["Diver"], Constant.TileStatus["Sunken"])

    self.tiles.update_tile(tileToUpdate)
    actual = self.tiles.get_tile(Constant.TileNames["IronGate"])

    self.assertEqual(tileToUpdate, actual)

