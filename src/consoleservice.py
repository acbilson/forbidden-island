from islandservice import *

class ConsoleService(IslandNotifier):
  
  def __init__(self, bus, io):
    IslandNotifier.__init__(self, bus)
    self.subscribedMessages.extend([MessageType.Console, MessageType.Initialize])
    self.io = io

  # TODO: Move this logic into a ConsoleBegin class or something
  #       options below should work from objects and call execute()
  #       on them
  def initialize(self, message):
    self.write_welcome()
    self.read_username()
    count = self.read_playercount()
    self.read_playertype(count)
    self.bus.receive(ScreenMessage("Initialization Complete"))

  def write_welcome(self):
    self.io.write("Welcome to Forbidden Island!\n\n")

  def read_username(self):
    self.io.write("What is your name? ")
    name = self.io.read()
    self.bus.receive(LogMessage("player's name is: " + name))

  def read_playercount(self):
    self.io.write("How many players will be playing? ")
    count = int(self.io.read())
    self.bus.receive(LogMessage(str(count) + " players should be created"))
    return count
 
  def read_playertype(self, count):
    self.io.write("Engineer, Pilot, Diver, Messenger, Explorer, Navigator\n")
    playerRequestCount = 0
    while playerRequestCount < count:
      self.io.write("Choose a player type: ")
      playerType = self.io.read()
      playerType = playerType.replace('\n', '')
      if not playerType in ["Engineer", "Pilot", "Diver", "Messenger", "Explorer", "Navigator"]:
        self.io.write("Not a valid player type.\n")
      else:
        self._sendPlayerCreateRequest(playerType)
        playerRequestCount = playerRequestCount + 1

  def _sendPlayerCreateRequest(self, playerType):
    request = Request("Create", { "type": playerType })
    self.bus.receive(PlayerMessage(request))
    self.bus.receive(LogMessage("Player type selected: " + str(playerType)))

  def on_message_received(self, message):
    options = {
      MessageType.Initialize: self.initialize
    }

    execute = options.get(message.type, self.nothing)
    response = execute(message)
    return response