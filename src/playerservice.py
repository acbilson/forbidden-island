from player import *
from islandservice import *

class PlayerService(IslandNotifier):

  def __init__(self, bus):
    IslandNotifier.__init__(self, bus)
    self.subscribedMessages.append(MessageType.Player)
    self.players = []

  def create_players(self, message):
    request = message.content
    if request.header == "Create":
      playerType = request.content['type']
      self.players.append(Player(playerType))

    self.bus.receive(LogMessage(str(message.content) + " players created"))
   
  def on_message_received(self, message):
    options = {
      MessageType.Player : self.create_players
    }

    execute = options.get(message.type, self.nothing)
    execute(message)
