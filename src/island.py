from constants import *
from player import *
from tile import *

class Island(object):

  TileNames = {
  "FoolsLanding": "FSL",
  "GoldGate": "GGT",
  "IronGate": "IGT",
  "BronzeGate": "BGT",
  "CopperGate": "CGT",
  "SilverGate": "SGT",
  "CoralPalace": "CLP",
  "TidalPalace": "TLP",
  "CaveOfShadows": "COS",
  "CaveOfEmbers": "COE",
  "WhisperingGarden": "WGD",
  "HowlingGarden": "HGD",
  "TempleOfTheSun": "TOS",
  "TempleOfTheMoon": "TOM",
  "MistyMarsh": "MYM",
  "Watchtower": "WTR",
  "BreakersBridge": "BKB",
  "CrimsonForest": "CFS",
  "Observatory": "OBS",
  "PhantomRock": "PMR",
  "TwilightHollow": "TLH",
  "CliffsOfAbandon": "COA",
  "DunesOfDeception": "DOD",
  "LostLagoon": "LLG"
  }

  Treasure = {
  "Empty": "|",
  "Earth": "E",
  "Water": "W",
  "Air": "A",
  "Fire": "F"
  }

  NameWidth = 3
  BoardWidth = 39
  EmptyTileSegment = '     '

  def __init__(self):
    self.board = Board.Empty
    self.tiles = []

  def generateBoard(self):
    
    """ randomly generates a filled board to begin play """

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

  def _getRandomNames(self):
    # Because it's converted from a dict to list, it's in random order
    return list(self.TileNames.values())

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
    for i,n in enumerate(allIndices):
      tile = Tile(n, names[i], PlayerType.Empty, TileStatus.Raised)
      self.tiles.append(tile)

  def getBoard(self):

    """ Returns the island board """

    return self.board

  # TODO: May simply pick this up from self.tiles later instead of generating it from the board
  def getTile(self, tileName):

    """ Retrieves a tile from the board by name """

    ni = self._findTileNameIndex(tileName)
    pi = self._findTilePlayerIndex(ni)
    si = self._findTileStatusIndex(ni)

    top = self._getValueFromIndex(ni)
    mid = self._getValueFromIndex(pi)
    bot = self._getValueFromIndex(si)

    return Tile(index=ni, name=top, player=mid, status=bot)

  def updateTile(self, newTile):

    """ Currently gets substrings for all non-tile pieces, then adds them back in the appropriate place.  Highly
    resource intensive, but no other way so far """

    segments = self._getIndexSegments(newTile, newTile.NameWidth)
    self._updateBoardWithTile(segments, newTile)

  def sinkTile(self, tileToSink):

    """ Currently gets substrings for all non-tile pieces, then adds them back in the appropriate place.  Seems
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
