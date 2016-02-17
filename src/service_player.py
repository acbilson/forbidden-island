from player import *
from service_island import *
from cards import *
from service_screen import ScreenOptions

class PlayerService(IslandNotifier):

  def __init__(self, bus, playerFactory, tiles):
    IslandNotifier.__init__(self, bus)
    self.subscribedMessages.append(MessageType.Player)
    self.players = []
    self.playerFactory = playerFactory
    self.tiles = tiles

  def create_players(self, message):

    """ Creates all players and sends their info to the ScreenService for a board update """

    playerTypes = message.request.content

    if playerTypes != None:
      players = self._add_players_to_list(playerTypes)
      self._add_players_to_tiles(players)
      message = self._get_screen_message(players)
      self.bus.receive(message)

  def _add_players_to_tiles(self, players):
    
    for p in players:
      tileToUpdate = self.tiles.get_tile(p.currentLocation)
      self.tiles.update_tile(tileToUpdate)

  def _add_players_to_list(self, playerTypes):

    players = []

    for playerType in playerTypes:
      player = self.playerFactory.get_instance(playerType)
      players.append(player)

    self.players.extend(players)
    return players

  def _get_screen_message(self, players):

    playersToCreate = []

    for player in players:
      playersToCreate.append((player.type, player.currentLocation))

    message = ScreenMessage(Request(ScreenOptions.AddPlayers, playersToCreate))
    return message
   
  def on_message_received(self, message):
    options = {
      PlayerOptions.Create : self.create_players
    }

    execute = options.get(message.request.header, self.nothing)
    execute(message)

class PlayerOptions():

  Create = "Create"
