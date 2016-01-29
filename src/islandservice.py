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
 
  def nothing(self, message):
    """ Log a report if a message is received which does not meet any of the expected criteria """
    errorMsg = str(type(self)) + " did nothing with message " + message.type.name + " with " + str(message.content)
    self.bus.receive(LogMessage(errorMsg))
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
