from enum import Enum

class Tile(object):

  MASTER_ID = 0
  Empty = '   '
  Sunken = '     '
  BoardWidth = 39
  NameWidth = 3
  SunkenWidth = 5

  def __init__(self, index, name, player, status):
    self.name = TileSegment(index, name)
    self.player = TileSegment(index + self.BoardWidth, player)
    self.status = TileSegment(index + (self.BoardWidth * 2), status)

    # Set a unique identifier
    self.id = self.MASTER_ID + 1

  def __eq__(self, other):
    if isinstance(other, self.__class__):
      return (self.name == other.name and 
              self.player == other.player and
              self.status == other.status)

  def __ne__(self, other):
    return not self.__eq__(other)

  def __str__(self):
    return "T(Name: " + str(self.name) + ", Player:" + str(self.player) + ", Status:" + str(self.status) + ")"

  def __repr__(self):
    return self.__str__()

  def getNameIndex(self):
    return self.name.index;

  def getPlayerIndex(self):
    return self.player.index;

  def getStatusIndex(self):
    return self.status.index;

  def getIndices(self):
    if(self.name.index != 0):
      return (self.name.index, self.player.index, self.status.index)
    
  def sink(self):

    """ Changes the contents of this tile to reflect a sunken state """

    self.name.value = self.Sunken
    self.player.value = self.Sunken
    self.status.value = self.Sunken
    self.name.index = self.name.index - 1
    self.player.index = self.player.index - 1
    self.status.index = self.status.index - 1

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

  def __str__(self):
    return "[" + str(self.index) + ", " + str(self.value) + "]"

  def __repr__(self):
    return __str__(self)
