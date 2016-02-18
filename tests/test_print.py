import sys
sys.path.append('../src')
from tiles import *
from tile import *

class Test(object):

    def __init__(self):
        self.board = ""


    def gen_board(self, tiles):

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
            segments.append(dividers[0] + rs.value + dividers[1])
            if len(rowSegments) != i:
                segments.append(TILE_SPACE)
            
        segments.append(space + '\n')

        if newLine != None:
            segments.append('\n')

        return segments

if __name__ == '__main__':

    tiles = Tiles()
    t = Test()
    board = t.gen_board(tiles.tiles)

    print(board)


