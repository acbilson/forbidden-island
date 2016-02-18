import random
from constants import *
from player import *
from tile import *

class Island(object):

  NameWidth = 3
  BoardWidth = 39
  EmptyTileSegment = '     '

  def generate_board(self, tiles):
    
    """ generates the board from the tiles given """

    segments = []

    rows = [[0,1], 
            [2,3,4,5], 
            [6,7,8,9,10,11],
            [12,13,14,15,16,17],
            [18,19,20,21],
            [22,23]]

    spaces = ['            ',
              '      ',
              '',
              '',
              '      ',
              '            ']

    names = [t.name for t in tiles]
    players = [t.player for t in tiles]
    statuses = [t.status for t in tiles]

    allSegs = []

    for i in range(0, len(rows)):
        nameSegments = self._gen_segments(rows[i], spaces[i], ('/', '\\'), names)
        playerSegments = self._gen_segments(rows[i], spaces[i], ('|', '|'), players)
        statusSegments = self._gen_segments(rows[i], spaces[i], ('\\', '/'), statuses, newLine=True)

        allSegs.append(''.join(nameSegments))
        allSegs.append(''.join(playerSegments))
        allSegs.append(''.join(statusSegments))

    return ''.join(allSegs)

  def _gen_segments(self, row, space, dividers, tileSegments, newLine=None):

    TILE_SPACE = ' '

    segments = []
    segments.append(space)

    last = row[len(row)-1]
    rowSegments = tileSegments[row[0]:last+1]

    for i,rs in enumerate(rowSegments):

        # Set get a unique icon for treasure - TODO: Should put this on Tile for when it's stolen
        if rs.value in Constant.TreasureTiles.keys():
            dividers = Constant.TreasureTiles.get(rs.value)

        segments.append(dividers[0] + rs.value + dividers[1])
        if len(rowSegments) != i:
            segments.append(TILE_SPACE)
        
    segments.append(space + '\n')

    if newLine != None:
        segments.append('\n')

    return segments
