import os
from constants import *
from islandservice import *
from tile import *

class ScreenService(IslandNotifier):
  
  def __init__(self, bus, island, cio):
    IslandNotifier.__init__(self, bus)
    self.subscribedMessages.append(MessageType.Screen)
    self.island = island
    self.io = cio

  def add_players(self, message):

    """ Adds players to the island board.  May move to island.py """

    playerTuple = message.request.content

    if playerTuple != None:
      for player, tile in playerTuple:
        self.island.add_players_to_board(tile, player)
    
    self.log(LogType.Info, str(len(playerTuple)) + " players added to the board")

  def render(self, message):

    """ Renders the island board to the screen """
    
    self.io.clear()
    self.io.write('\n')
    self.io.write(self.island.board)

    self.log(LogType.Info, "Screen rendered")


  def on_message_received(self, message):
    options = {
      ScreenOptions.Render: self.render,
      ScreenOptions.AddPlayers: self.add_players
    }

    execute = options.get(message.request.header, self.nothing)
    execute(message)
    self.render(None)

class ScreenOptions():

  Render = "Render"
  AddPlayers = "Add Players"
