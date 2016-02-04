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
    self.generateBoard()

  def generateBoard(self):
    
    """ randomly generates a filled board to begin play.  Runs once """

    # If the board is already generated, do not generate again
    if self.board != Board.Empty:
      return None

    tileNames = self._getRandomNames()
    self._generateTiles(tileNames)

    # Splits the board into segments that can be pieced into a cohesive whole
    tileSegments = []

    # Piece the board together from a combination of the tiles and its segments 

    # Add the first segment
    firstSegment = self.board[0:self.tiles[0].name.index]
    tileSegments.append(firstSegment)

    for i in range(0, len(self.tiles)-1):
      # Append the tile name, then the next segment
      tileSegments.append(self.tiles[i].name.value)
      segStart = self.tiles[i].name.index + self.NameWidth
      segEnd = self.tiles[i+1].name.index
      tileSegment = self.board[segStart:segEnd]
      tileSegments.append(tileSegment)

    # Add the last tile and segment
    lastTileIndex = len(self.tiles) - 1
    tileSegments.append(self.tiles[lastTileIndex].name.value)
    segStart = self.tiles[lastTileIndex].name.index + self.NameWidth
    segEnd = len(self.board)
    lastSegment = self.board[segStart:segEnd]
    tileSegments.append(lastSegment)

    # Turn all segments into one string to create the board
    self.board = ''.join([s for s in tileSegments])

    hasRun = True

  def _getRandomNames(self):
    # Because it's converted from a dict to list, it's in random order
    return list(Constant.TileNames.values())

  def _generateTiles(self, names):

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

  def getBoard(self):

    """ Returns the island board """

    return self.board

  def add_players_to_board(self, tileName, playerType):
    tileToUpdate = self.getTile(tileName)
    tileToUpdate.player.value = playerType
    self.updateTile(tileToUpdate)

  # TODO: implement method to add treasure to the board (may be called in generateBoard)
  def add_treasure_to_board(self):
    pass

  def getTile(self, tileName):

    """ Retrieves a tile from the board by name """

    tile = self._get_tile_by_list(tileName)

    # Retrieve by index if board is not generated TODO: DEPRECIATE 
    if tile == None:
      tile = self._get_tile_by_index(tileName)

    return tile

  def _get_tile_by_list(self, tileName):

    """ Retrieves a tile from the tile list - faster """

    tiles = [t for t in self.tiles if t.name.value == tileName]
    if len(tiles) > 0:
      return tiles[0]
    else:
      return None

  def _get_tile_by_index(self, tileName):
    
    """ Retrieves a tile from the board by name - slower but necessary if board hasn't been generated """

    ni = self._findTileNameIndex(tileName)
    pi = self._findTilePlayerIndex(ni)
    si = self._findTileStatusIndex(ni)

    top = self._getValueFromIndex(ni)
    mid = self._getValueFromIndex(pi)
    bot = self._getValueFromIndex(si)

    return Tile(index=ni, name=top, player=mid, status=bot)

  # TODO: implement.  Should be some way of stripping the cursor's location left/right, placing the cursor in the new
  # spot, then snapping the two ends back on.  Similar to updateTile, only fewer segments
  def updateCursor(self, cursor):
    pass

  def updateTile(self, newTile):

    """ Gets substrings for all non-tile pieces, then adds them back in the appropriate place.  Highly
    resource intensive, but no other way so far """

    segments = self._getIndexSegments(newTile, newTile.NameWidth)
    self._updateBoardWithTile(segments, newTile)

  def sinkTile(self, tileToSink):

    """ Gets substrings for all non-tile pieces, then adds them back in the appropriate place.  Seems
    resource intensive, but no other way so far """

    tileToSink.sink()

    segments = self._getIndexSegments(tileToSink, tileToSink.SunkenWidth)
    self._updateBoardWithTile(segments, tileToSink)

  def _updateBoardWithTile(self, segments, newTile):
    self.board = (segments[0] + newTile.name.value + 
                  segments[1] + newTile.player.value + 
                  segments[2] + newTile.status.value + 
                  segments[3])

  def _getIndexSegments(self, tile, tileSpacing):

    leftTop = self.board[0:tile.name.index]
    rightTop = self.board[tile.name.index+tileSpacing:tile.player.index]
    rightMid = self.board[tile.player.index+tileSpacing:tile.status.index]
    rightBot = self.board[tile.status.index+tileSpacing:len(self.board)]

    segments = (leftTop, rightTop, rightMid, rightBot)
    return segments

  def _findTileNameIndex(self, tileName):
    return self.board.index(tileName)

  def _findTilePlayerIndex(self, nameIndex):
    return nameIndex + self.BoardWidth

  def _findTileStatusIndex(self, nameIndex):
    return nameIndex + (self.BoardWidth*2)

  def _getValueFromIndex(self, index):
    start = index
    end = index + self.NameWidth
    return self.board[start:end]
