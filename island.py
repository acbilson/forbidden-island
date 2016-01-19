class Island(object):

  NameWidth = 3
  BoardWidth = 39

  def __init__(self):
    self.board = Constants.EmptyBoard

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

    ni = self._findTileNameIndex(tileName)
    pi = self._findTilePlayerIndex(ni)
    si = self._findTileStatusIndex(ni)

    leftTop = self.board[0:ni-1]
    rightTop = self.board[ni+self.NameWidth+1:pi-1]
    rightMid = self.board[pi+self.NameWidth+1:si-1]
    rightBot = self.board[si+self.NameWidth+1:len(self.board)]

    self.board = (leftTop + newTile.getTop() + rightTop + newTile.getMid() + rightMid + newTile.getBot() + rightBot)


  # Remove the tile entirely from the game board by replacing it with spaces
  # def sinkTile()


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

  def get(self):
    return self.board

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
