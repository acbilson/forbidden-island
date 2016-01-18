class Island(object):

  NameWidth = 3
  BoardWidth = 39

  def __init__(self):
    self.board = Constants.EmptyBoard

  def getTile(self, tileName):
    i = self._findTileNameIndex(tileName)
    top = self._getTileName(i)
    mid = self._getTileUser(i)
    bot = self._getTileStatus(i)
    return Tile(name=top, player=mid, status=bot)

  def updateTile(self, tile):
    """ Currently gets substrings for all non-tile pieces, then adds them back in the appropriate place.  Highly
    resource intensive, but no other way so far """
    ni = self._findTileNameIndex(tile.name)
    pi = self._findTilePlayerIndex(ni)
    # print("pi is: ", pi, "actual is: ", self.board.index('ENG'))
    si = self._findTileStatusIndex(ni)
    # print("si is: ", si, "actual is: ", self.board.index('SNK'))

    leftTop = self.board[0:ni-1]
    rightTop = self.board[ni+self.NameWidth+1:pi-1]
    rightMid = self.board[pi+self.NameWidth+1:si-1]
    rightBot = self.board[si+self.NameWidth+1:len(self.board)]

    self.board = (leftTop + tile.getTop() + rightTop + tile.getMid() + rightMid + tile.getBot() + rightBot)
    # print(leftTop + '/COA\\' + rightTop + '|ENG|' + rightMid + '\   /' + rightBot)

  def _findTileNameIndex(self, tileName):
    return self.board.index(tileName)

  def _findTilePlayerIndex(self, nameIndex):
    return nameIndex + self.BoardWidth

  def _findTileStatusIndex(self, nameIndex):
    return nameIndex + (self.BoardWidth*2)

  def _getTileName(self, index):
    start = index
    end = index + self.NameWidth
    return self.board[start:end]

  def _getTileUser(self, index):
    start = index + self.BoardWidth
    end = (index + self.NameWidth) + self.BoardWidth
    return self.board[start:end]

  def _getTileStatus(self, index):
    start = index + (self.BoardWidth * 2)
    end = (index + self.NameWidth) + (self.BoardWidth * 2)
    return self.board[start:end]

  def get(self):
    return self.board

class TileName():
  CliffsOfAbandon = "COA"

class PlayerType():
  Engineer = "ENG"

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
    return '|' + self.player + '|'

  def getBot(self):
    return '\\' + self.status + '/'



class Constants():

  EmptyBoard = (
  '            /   \ /   \\\n' + 
  '            |   | |   |\n' +
  '            \   / \   /\n' +
  '\n' + 
  '     /   \ /   \ /   \ /   \\\n' + 
  '     |   | |   | |   | |   |\n' + 
  '     \   / \   / \   / \   /\n' +
  '\n' +
  '/   \ /   \ /   \ /   \ /   \ /   \\\n' +
  '|   | |   | |   | |   | |   | |   |\n' +
  '\   / \   / \   / \   / \   / \   /\n' +
  '\n' +
  '/   \ /   \ /   \ /   \ /   \ /   \\\n' +
  '|   | |   | |   | |   | |   | |   |\n' +
  '\   / \   / \   / \   / \   / \   /\n' +
  '\n' +
  '      /   \ /   \ /   \ /   \\\n' +
  '      |   | |   | |   | |   |\n' +
  '      \   / \   / \   / \   /\n' +
  '\n' +
  '            /   \ /   \\\n' +
  '            |   | |   |\n' +
  '            \   / \   /\n')
