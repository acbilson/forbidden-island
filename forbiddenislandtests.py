import sys
sys.path.append("C:\\SourceCode\\PersonalRepo\\Python\\PyLexLib")
from iofactory import *

import unittest
from island import *

class TestIsland(unittest.TestCase):

  """ Testing the Island class """
  island = None

  def setUp(self):
    self.island = Island()

  def test_island_ctor(self):
    island = Island()

  def test_island_getTile(self):
    self.island.board = TestConstants.GetTileBoard

    actual = self.island.getTile(TileName.CliffsOfAbandon)

    expected = Tile(name=TileName.CliffsOfAbandon, 
                    player=PlayerType.Engineer, 
                    status=TileStatus.Sunken)

    self.assertEqual(expected, actual)

  def test_island_updateTile(self):
    self.island.board = TestConstants.GetTileBoard
    tile = Tile(name=TileName.DunesOfDeception, 
                player=PlayerType.Pilot, 
                status=TileStatus.Raised)

    self.island.updateTile(TileName.CliffsOfAbandon, tile)

    expected = TestConstants.UpdateTileBoard
    self.assertEqual(expected, self.island.board)

class TestTile(unittest.TestCase):
  """ Testing the Tile class """
  tile = None

  def setUp(self):
    self.tile = Tile()

  def test_tile_ctor(self):
    tile = Tile()

    self.assertIsNotNone(tile.name)

  def test_tile_get(self):
    tile = Tile()

    actual = tile.get()

    expected = ('/   \\' +
                '|   |'  +
                '\   /')

    self.assertEqual(expected, actual)

  def test_tile_get_allValuesSet(self):
    tile = Tile(name=TileName.DunesOfDeception, 
                player=PlayerType.Pilot, 
                status=TileStatus.Sunken)

    actual = tile.get()

    expected = ('/DOD\\' +
                '|PLT|'  +
                '\SNK/')

    self.assertEqual(expected, actual)


  def test_tile_get_hasTreasure(self):
    tile = Tile(name=TileName.TempleOfTheMoon)

    actual = tile.get()

    expected = ('/TOM\\' +
                'R   R'  +
                '\   /')

    self.assertEqual(expected, actual)


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
