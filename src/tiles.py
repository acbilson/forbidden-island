import random
from constants import *
from player import *
from tile import *

class Tiles(object):

  EmptyTileSegment = '     '

  def __init__(self):
    self.tiles = []
    self._generate_tiles()

  def _generate_tiles(self):
    
    """ randomly generates tiles to begin play.  Runs at init """

    if len(self.tiles) == 0:
        tileNames = self._get_random_names()
        self._gen_tiles_by_name(tileNames)
        self.sink_first_tiles()

  def sink_first_tiles(self):
    tiles = self._get_random_tiles()
    for t in tiles:
      t.status.value = Constant.TileStatus["Sunken"]
      self.update_tile(t)

  def _get_random_tiles(self):

    """ Gets six random tiles, the ones that will be sunken at the beginning """

    names = self._get_random_names()
    indices = self._getRandomIndices(6)

    sixNames = []
    
    for i,n in enumerate(names):
      if (i in indices):
        sixNames.append(n)

    sixTiles = [t for t in self.tiles if t.name.value in sixNames]

    return sixTiles
    
  def _get_random_names(self):
    # Because it's converted from a dict to list, it's in random order
    return list(Constant.TileNames.values())

  def _getRandomIndices(self, number):

    endOfRange = len(self.tiles)
    indices = []

    while len(indices) < number:
      randomNumber = random.randrange(endOfRange)
      # Makes sure all random numbers are unique
      if not randomNumber in indices:
        indices.append(randomNumber)
      
    return indices

  def _gen_tiles_by_name(self, names):

    # Index pattern in space between indices
    # 14 + 6 + 
    # 144 + 6(3x) + 
    # 132 + 6(5x) + 
    # 126 + 6(5x) + 
    # 132 + 6(3x) + 
    # 144 + 6
    allIndices = [14, 20,
                  164, 170, 176, 182,
                  314, 320, 326, 332, 338, 344,
                  470, 476, 482, 488, 494, 500,
                  632, 638, 644, 650,
                  794, 800]

    # Creates a tile for every index
    for i,index in enumerate(allIndices):
      tile = Tile(index, names[i], Constant.PlayerType["Empty"], Constant.TileStatus["Raised"])
      self.tiles.append(tile)

  def get_tile(self, tileName):

    """ Retrieves a tile from the board by name """

    tiles = [t for t in self.tiles if t.name.value == tileName]

    if len(tiles) > 0:
      return tiles[0]
    else:
      return None

  def update_tile(self, newTile):

    """ Updates a tile with the new tile's contents """

    for i,t in enumerate(self.tiles):
        if t.name.value == newTile.name.value:
            self.tiles[i] = newTile

  def sink_tile(self, tileName):

    """ Sinks the tile by name """

    tileToSink = self.get_tile(tileName)
    if tileToSink != None:
        tileToSink.sink()
