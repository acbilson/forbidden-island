from islandservice import *

class ScreenService(IslandNotifier):
  
  def __init__(self, bus, island, cio):
    IslandNotifier.__init__(self, bus)
    self.subscribedMessages.append(MessageType.Console)
    self.island = island
    self.io = cio

  def render(self, message):
    if message.content == "Initialization Complete":
      # Add players to the board at their appropriate spots
      # Let ConsoleService know to query the user for the player's next action
      self.io.write("\n\tLet the game begin!\n\n")
      self.io.write(self.island.board)

    elif message.content == "Render":
      self.io.write(self.island.board)

  def on_message_received(self, message):
    options = {
      MessageType.Console : self.render
    }

    execute = options.get(message.type, self.nothing)
    execute(message)
