# from collections import deque
from queue import Queue
from constants import * 
from message import *

class IslandSubscriber(object):

  """ Mixin class to subscribe to messages from the IslandBus """

  def __init__(self):
    self.lastMessage = None
    self.subscribedMessages = []

  def subscribe(self, bus):

    """ Adds this subscriber to this bus' queue """

    bus.add_subscriber(self)

  def on_message_received(self, message):
    """ Event the bus will raise when a message applies to this subscriber """
    pass

class IslandNotifier(IslandSubscriber):

  """ Mixin class to send messages to an instance of the IslandBus """

  def __init__(self, bus):
    IslandSubscriber.__init__(self)
    self.bus = bus
    # From parent
    self.subscribe(self.bus)

  def notify(self, message):

    """ Notifies the bus to add this message to its queue """

    self.bus.receive(message)

class ConsoleService(IslandNotifier):
  
  def __init__(self, bus, io):
    IslandNotifier.__init__(self, bus)
    self.subscribedMessages.append(MessageType.All)
    self.io = io

  # TODO: Move this logic into a ConsoleBegin class or something
  #       options below should work from objects and call execute()
  #       on them
  def initialize(self):
    self.write_welcome()
    self.read_username()
    count = self.read_playercount()
    self.read_playertype(count)
    self.bus.receive(ConsoleMessage("Initialization Complete"))

  def write_welcome(self):
    self.io.write("Welcome to Forbidden Island!\n\n")

  def read_username(self):
    self.io.write("What is your name? ")
    name = self.io.read()
    self.bus.receive(ConsoleMessage("name: " + name))

  def read_playercount(self):
    self.io.write("How many players will be playing? ")
    count = int(self.io.read())
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

  def on_message_received(self, message):
    options = {
      MessageType.Initialize: self.initialize
    }

    execute = options.get(message.type, lambda: "nothing")
    response = execute()
    return response

from player import *

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
    
  def nothing(self, message):
    errorMsg = str(type(self)) + " did nothing with message " + message.type.name + " with " + str(message.content)
    self.bus.receive(LogMessage(errorMsg))
    pass

  def on_message_received(self, message):
    options = {
      MessageType.Player : self.create_players
    }

    execute = options.get(message.type, self.nothing)
    execute(message)

class ScreenService(IslandNotifier):
  
  def __init__(self, bus):
    IslandNotifier.__init__(self, bus)
    self.subscribedMessages.append(MessageType.All)

  def on_message_received(self, message):
    pass

class LogService(IslandNotifier):
  
  def __init__(self, bus, io):
    IslandNotifier.__init__(self, bus)
    self.io = io
    self.subscribedMessages.append(MessageType.All)
    self.subscribedMessages.append(MessageType.Log)
    self.log = []

  def on_message_received(self, message):
    entry = "Type: " + message.type.name + " Content: " + str(message.content) + '\n'
    self.log.append(entry)

  def print_all(self):
    print("\nDebug Report:")
    for i,l in enumerate(self.log):
      report = str(i) + ": " + l
      self.io.write(report)

