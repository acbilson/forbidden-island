import sys
from service_island import *
from service_screen import ScreenOptions
from service_player import PlayerOptions

class ConsoleService(IslandNotifier):
  
  # TODO: pass a ConsoleParser class to handle input
  def __init__(self, bus, io):
    IslandNotifier.__init__(self, bus)
    self.subscribedMessages.extend([MessageType.Console, MessageType.Initialize])
    self.io = io

  def initialize(self, message):
    self.write_welcome()
    self.read_username()
    count = self.read_playercount()
    addPlayersMessage = self.read_playertype(count)
    self.bus.receive(addPlayersMessage)

  def write_welcome(self):
    self.io.write("Welcome to Forbidden Island!\n\n")

  def read_username(self):
    self.io.write("What is your name? ")
    name = self.io.read()

    self.log(LogType.Info, "User's Name is: " + name)

  def read_playercount(self):
    self.io.write("How many players will be playing? ")
    count = int(self.io.read())

    self.log(LogType.Info, str(count) + " players should be created")

    return count
 
  def read_playertype(self, count):

    """ Reads each player type from the user, returning a list of players for the PlayerService to create """

    self.io.write("Engineer, Pilot, Diver, Messenger, Explorer, Navigator\n")
    playersAdded = 0
    allPlayerTypes = []

    # Keeps requesting input until all players are chosen 
    while playersAdded < count:
      self.io.write("Choose a player type: ")
      value = self.io.read()
      value = value.strip()

      playerType = Constant.PlayerType.get(value)

      if playerType != None:
        allPlayerTypes.append(playerType)
        playersAdded = playersAdded + 1
      else:
        self.io.write("Not a valid player type.\n")

      createMessage = PlayerMessage(Request(PlayerOptions.Create, allPlayerTypes))
    return createMessage

  def _is_valid_playertype(self, playerType):
      return playerType in ["Engineer\n", "Pilot\n", "Diver\n", "Messenger\n", "Explorer\n", "Navigator\n"]

  def exit(self, message):
    sys.exit()

  # TODO: Implement this
  def next(self, message):
    pass

  def on_message_received(self, message):
    options = {
      MessageType.Initialize: self.initialize,
      MessageType.Exit: self.exit,
      MessageType.Console: self.next
    }

    execute = options.get(message.type, self.nothing)
    response = execute(message)
    return response
