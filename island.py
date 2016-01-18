class Island(object):

  def __init__(self):
    self.name = "Test"

class TileName():
  CliffsOfAbandon = "COA"

class Tile(object):

  Empty = '   '

  def __init__(self, name):
    self.name = name
    self.player = self.Empty
    self.status = self.Empty

  def get(self):
    top = self._addTop()
    mid = self._addMid()
    bot = self._addBot()
    return (top + mid + bot)

  def _addTop(self):
    return '/' + self.name + '\\'

  def _addMid(self):
    return '|' + self.player + '|'

  def _addBot(self):
    return '\\' + self.status + '/'
