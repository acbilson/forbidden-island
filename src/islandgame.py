import sys
sys.path.append('C:\SourceCode\PersonalRepo\Python\PyLexLib')
from iofactory import *
from islandbus import *
from screenservice import *
from consoleservice import *
from playerservice import *
from logservice import *
from island import *

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
      self.bus.receive(ExitMessage())
  
if __name__ == "__main__":

  cio = IOFactory().GetInstance()
  bus = IslandBus()
  factory = MessageFactory()
  island = Island()
  playerDeck = PlayerDeck()

  # Each service registers with the bus within their ctor
  ss = ScreenService(bus, island, cio)
  cs = ConsoleService(bus, cio)
  ps = PlayerService(bus, playerDeck)
  ls = LogService(bus, cio)

  game = IslandGame(bus, factory)

  game.play()

  ls.print_all()
