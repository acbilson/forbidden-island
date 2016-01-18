import unittest
from island import *

class TestIsland(unittest.TestCase):

  """ Testing the Island class """

  def setup(self):
    self.island = Island()

  def test_island_ctor(self):
    island = Island()
      
class TestTile(unittest.TestCase):

  """ Testing the Tile class """
  tile = None

  def setUp(self):
    self.tile = Tile("COA")

  def test_tile_ctor(self):
    tile = Tile("COA")

    self.assertIsNotNone(tile.name)

  def test_tile_get(self):
    tile = Tile("COA")

    actual = tile.get()

    expected = ('/COA\\' +
                '|   |'  +
                '\   /')

    self.assertEqual(expected, actual)
