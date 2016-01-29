import sys
sys.path.append('C:\SourceCode\PersonalRepo\Python\PyLexLib')
from iofactory import *
from islandbus import *

class IslandGame(object):
  """ Central class for the Forbidden Island game, where the game loop executes """

  def __init__(self, bus, messageFactory):
    self.bus = bus
    self.messageFactory = messageFactory

  def play(self):
    self.bus.receive(StartMessage())

    exitCode = 0
    while(exitCode == 0):
      exitCode = self.bus.listen()
  
if __name__ == "__main__":

  cio = IOFactory().GetInstance()
  bus = IslandBus()
  factory = MessageFactory()

  # Each service registers with the bus within their ctor
  # is = IslandService(bus, island)
  cs = ConsoleService(bus, cio)
  ps = PlayerService(bus)
  ls = LogService(bus, cio)

  game = IslandGame(bus, factory)

  game.play()

  ls.print_all()
