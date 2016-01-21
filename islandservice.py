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

  # Rename
  def on_message_received(self, message):
    """ Event the notifier will raise when a message applies to this subscriber """
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

  def print_welcome(self):
    self.io.write("Welcome to Forbidden Island!\n")
    
  def move_player(self):
    pass

  def on_message_received(self, message):
    options = {
      MessageType.Initialize: self.print_welcome,
      MessageType.Console_Move: self.move_player
    }

    response = options.get(message.type, lambda: "nothing")
    response()


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
    self.log = []

  def on_message_received(self, message):
    entry = "Type: " + message.type.name + "Content: " + message.content + '\n'
    self.log.append(entry)

  def print_all(self):
    for l in self.log:
      self.io.write(l)
