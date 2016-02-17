import os
from constants import *
from service_island import *
from tile import *

class ScreenService(IslandNotifier):
  
  def __init__(self, bus, island, cio, tiles):
    IslandNotifier.__init__(self, bus)
    self.subscribedMessages.append(MessageType.Screen)
    self.island = island
    self.io = cio
    self.tiles = tiles

  def render(self, message):

    """ Renders the island board to the screen """
    
    self.io.clear()
    board = self.island.generate_board(self.tiles)
    self.io.write('\n')
    self.io.write(board)

    self.log(LogType.Info, "Screen rendered")

  def on_message_received(self, message):
    options = {
      ScreenOptions.Render: self.render,
    }

    execute = options.get(message.request.header, self.nothing)
    execute(message)

class ScreenOptions():

  Render = "Render"
