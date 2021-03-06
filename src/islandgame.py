from iofactory import *
from service_island import *
from service_console import *
from service_player import *
from service_log import *
from service_screen import *
from playerfactory import *
from islandbus import *
from island import *
from tiles import *

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
      self.start_next()
      self.bus.listen()
      self.bus.receive(ExitMessage())

  def start_next(self):
    message = ConsoleMessage(Request("Next Action"))
    self.bus.receive(message)
  
if __name__ == "__main__":

  cio = IOFactory().GetInstance()
  bus = IslandBus()
  messageFactory = MessageFactory()
  playerFactory = PlayerFactory()
  island = Island()
  playerDeck = PlayerDeck()
  tiles = Tiles()

  # Each service registers with the bus within their ctor
  ss = ScreenService(bus, island, cio, tiles)
  cs = ConsoleService(bus, cio)
  ps = PlayerService(bus, playerFactory, tiles)
  ls = LogService(bus, cio)

  game = IslandGame(bus, messageFactory)

  game.play()

  ls.print_all()
