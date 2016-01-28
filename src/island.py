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

  NameWidth = 3
  BoardWidth = 39
  EmptyTileSegment = '     '

  def __init__(self):
    self.board = Board.Empty
    self.newBoard = ""

  def generateBoard(self):
    
    """ randomly generates a filled board to begin play """

    # Randomize the indices
    tileNames = list(self.TileNames.values())

    allIndices = [14, 20,
                  163, 169, 175, 181,
                  314, 320, 326, 332, 338, 344,
                  470, 476, 482, 488, 494, 500,
                  632, 638, 644, 650,
                  794, 800]
    tiles = []

    for i,n in enumerate(allIndices):
      tile = Tile(n, tileNames[i], PlayerType.Empty, TileStatus.Raised)
      tiles.append(tile)

    tileSegments = []

    firstSegment = self.board[0:allIndices[0]]
    tileSegments.append(firstSegment)

    for i,t in enumerate(tiles):
      tileSegments.append(t.name.value)
      segStart = t.name.index + self.NameWidth
      segEnd = tiles[i].name.index
      segment = self.board[segStart:segEnd]
      # print(segStart, '\t', segEnd, '\t*', segment, '*')
      tileSegments.append(segment)

    # for i in range(1, len(allIndices)-1):
      # # Append the tile name
      # tileSegments.append(allNames[i])
      # # Append the next segment
      # segStart = allIndices[i] + self.NameWidth
      # segEnd = allIndices[i+1]
      # tileSegment = self.board[segStart:segEnd]
      # tileSegments.append(tileSegment)

    start = len(allIndices)
    end = len(self.board)
    lastSegment = self.board[start:end]
    tileSegments.append(lastSegment)

    # Turn the segments into one string
    # [print(s) for s in tileSegments]
    self.newBoard = ''.join([s for s in tileSegments])

  def getBoard(self):

    """ Returns the island board """

    return self.board

  def getTile(self, tileName):

    """ Retrieves a tile from the board by name """

    ni = self._findTileNameIndex(tileName)
    pi = self._findTilePlayerIndex(ni)
    si = self._findTileStatusIndex(ni)

    top = self._getValueFromIndex(ni)
    mid = self._getValueFromIndex(pi)
    bot = self._getValueFromIndex(si)

    return Tile(index=ni, name=top, player=mid, status=bot)

  def updateTile(self, tileName, newTile):

    """ Currently gets substrings for all non-tile pieces, then adds them back in the appropriate place.  Highly
    resource intensive, but no other way so far """

    indices = self._getIndexSegments(tileName)
    self._updateBoardWithNewTile(indices, newTile)

  def sinkTile(self, tileName):

    """ Currently gets substrings for all non-tile pieces, then adds them back in the appropriate place.  Highly
    resource intensive, but no other way so far """

    indices = self._getIndexSegments(tileName)
    self._updateBoardWithMissingTile(indices)

  def _updateBoardWithNewTile(self, indices, newTile):
    self.board = (indices[0] + newTile.name.value + 
                  indices[1] + newTile.player.value + 
                  indices[2] + newTile.status.value + 
                  indices[3])

  def _updateBoardWithMissingTile(self, indices):
    self.board = (indices[0] + self.EmptyTileSegment + 
                  indices[1] + self.EmptyTileSegment + 
                  indices[2] + self.EmptyTileSegment + 
                  indices[3])

  def _getIndexSegments(self, tileName):

    ni = self._findTileNameIndex(tileName)
    pi = self._findTilePlayerIndex(ni)
    si = self._findTileStatusIndex(ni)

    leftTop = self.board[0:ni-1]
    rightTop = self.board[ni+self.NameWidth+1:pi-1]
    rightMid = self.board[pi+self.NameWidth+1:si-1]
    rightBot = self.board[si+self.NameWidth+1:len(self.board)]

    indices = (leftTop, rightTop, rightMid, rightBot)
    return indices

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
