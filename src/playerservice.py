from player import *
from islandservice import *
from cards import *
from screenservice import ScreenOptions

class PlayerService(IslandNotifier):

  def __init__(self, bus, deck):
    IslandNotifier.__init__(self, bus)
    self.subscribedMessages.append(MessageType.Player)
    self.players = []
    self.deck = deck

  def create_players(self, message):

    """ Creates all players and sends their info to the ScreenService for a board update """

    playerTypes = message.request.content

    if playerTypes != None:
      players = self._add_players_to_list(playerTypes)
      message = self._get_screen_message(players)
      self.bus.receive(message)

  def _add_players_to_list(self, playerTypes):

    players = []

    for playerType in playerTypes:
      players.append(Player(playerType))

    self.players.extend(players)
    return players

  def _get_screen_message(self, players):

    playersToCreate = []

    for player in players:
      playerLocation = player.get_start_location()
      playersToCreate.append((player.type, playerLocation))

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
