from player import *
from islandservice import *

class PlayerService(IslandNotifier):

  def __init__(self, bus):
    IslandNotifier.__init__(self, bus)
    self.subscribedMessages.append(MessageType.Player)
    self.players = []

  def create_players(self, message):
    if message.request.header == "Create":
      playerType = message.request.content['type']
      self.players.append(Player(playerType))

    message = LogMessage(Request("Info", str(message.request.content) + " players created"))
    self.bus.receive(message)
   
  def on_message_received(self, message):
    options = {
      MessageType.Player : self.create_players
    }

    execute = options.get(message.type, self.nothing)
    execute(message)
