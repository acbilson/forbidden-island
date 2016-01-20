from constants import *
from island import *

class Tile(object):

  Empty = '   '
  BoardWidth = 39

  def __init__(self, index, name, player, status):
    self.name = TileSegment(index, name)
    self.player = TileSegment(index + self.BoardWidth, player)
    self.status = TileSegment(index + (self.BoardWidth * 2), status)

  def __eq__(self, other):
    if isinstance(other, self.__class__):
      return (self.name == other.name and 
              self.player == other.player and
              self.status == other.status)

  def __ne__(self, other):
    return not self.__eq__(other)

  def getNameIndex(self):
    return self.name.index;

  def getPlayerIndex(self):
    return self.player.index;

  def getStatusIndex(self):
    return self.status.index;

  def getIndices(self):
    if(self.name.index != 0):
      return (self.name.index, self.player.index, self.status.index)
    
class TileSegment(object):

  def __init__(self, index, value):
    self.index = index
    self.value = value

  def __eq__(self, other):
    if isinstance(other, self.__class__):
      return (self.index == other.index and
              self.value == other.value)

  def __ne__(self, other):
    return not self.__eq__(other)
