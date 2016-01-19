class Island(object):

  NameWidth = 3
  BoardWidth = 39
  EmptyTileSegment = '     '

  def __init__(self):
    self.board = Constants.EmptyBoard
    self.newBoard = ""

  def generateBoard(self):
    
    """ randomly generates a filled board to begin play """

    # Get All indices that will be filled
    # Randomize the indices
    # Place each name value into one of the indices

    allIndices = [0, 14, 20,
                  47, len(self.board)]

    tileSegments = []

    for i in range(0, len(allIndices)-1):
      tileSegment = self.board[allIndices[i]:allIndices[i+1]]
      tileSegments.append(tileSegment)
      tileSegments.append("XXX")

    self.newBoard = ''.join([str(s) for s in tileSegments])

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

    return Tile(name=top, player=mid, status=bot)

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
    self.board = (indices[0] + newTile.getTop() + 
                  indices[1] + newTile.getMid() + 
                  indices[2] + newTile.getBot() + 
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

class TileName():
  CliffsOfAbandon = "COA"
  DunesOfDeception = "DOD"

class PlayerType():
  Engineer = "ENG"
  Pilot = "PLT"

class TileStatus():
  Sunken = "SNK"
  Raised = "   "

class Tile(object):

  Empty = '   '

  def __init__(self, name=Empty, player=Empty, status=Empty):
    self.name = name
    self.player = player
    self.status = status

  def __eq__(self, other):
    if isinstance(other, self.__class__):
      return (self.name == other.name and 
              self.player == other.player and
              self.status == other.status)

  def __ne__(self, other):
    return not self.__eq__(other)

  def get(self):
    top = self.getTop()
    mid = self.getMid()
    bot = self.getBot()
    return (top + mid + bot)

  def getTop(self):
    return '/' + self.name + '\\'

  def getMid(self):
    if self.name in ['TOS', 'TOM']:
      return 'R' + self.player + 'R'
    return '|' + self.player + '|'

  def getBot(self):
    return '\\' + self.status + '/'

class TileName():
  CliffsOfAbandon = "COA"
  DunesOfDeception = "DOD"
  TempleOfTheSun = "TOS"
  TempleOfTheMoon = "TOM"

class PlayerType():
  Engineer = "ENG"
  Pilot = "PLT"
  Diver = "DVR"

class TileStatus():
  Raised = "   "
  Sunken = "SNK"
  Lost = "LST"

class Constants():

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
