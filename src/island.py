import random
from constants import *
from player import *
from tile import *

class Island(object):

  NameWidth = 3
  BoardWidth = 39
  EmptyTileSegment = '     '

  def __init__(self):
    self.tiles = []
    self.board = Board.Empty

  def generate_board(self, tiles):
    
    """ generates the board from the tiles given """

    import pdb
    pdb.set_trace()
    # Get list of tiles instead of Tiles obj
    tiles = tiles.tiles

    # Splits the board into segments that can be pieced into a cohesive whole
    tileSegments = []

    # Piece the board together from a combination of the tiles and its segments 

    # Add the first segment
    firstSegment = self.board[0:tiles[0].name.index]
    tileSegments.append(firstSegment)

    for i in range(0, len(tiles)-1):
      # Append the tile name, then the next segment
      tileSegments.append(tiles[i].name.value)
      segStart = tiles[i].name.index + self.NameWidth
      segEnd = tiles[i+1].name.index
      # TODO: Must add the other values, not just the name
      tileSegment = self.board[segStart:segEnd]
      tileSegments.append(tileSegment)

    # Add the last tile and segment
    lastTileIndex = len(tiles) - 1
    tileSegments.append(tiles[lastTileIndex].name.value)
    segStart = tiles[lastTileIndex].name.index + self.NameWidth
    segEnd = len(self.board)
    lastSegment = self.board[segStart:segEnd]
    tileSegments.append(lastSegment)

    # Turn all segments into one string to create the board
    self.board = ''.join([s for s in tileSegments])
    return self.board
