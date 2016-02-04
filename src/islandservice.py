from queue import Queue
from constants import * 
from message import *

# I separated these into two in order to make it possible to have a subscriber that cannot notify.  In hindsight,
# perhaps the LogService should be one of these?
# TODO: Descend LogService from IslandSubscriber instead of IslandNotifier

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

    # TODO: Add raise NotImplementedException()
    pass

  def on_error_received(self, error):
    pass
 
  # TODO: Rename to something more descriptive
  def nothing(self, message):

    """ Log a report if a message is received which does not meet any of the expected criteria.  This is being used to
    standardize the way all services handle messages they receive but do not act upon """

    errorMsg = str(type(self)) + " did nothing with message " + message.type.name + " with " + str(message.request)
    self.bus.receive(LogMessage(Request("Error", errorMsg)))

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

  def log(self, logType, message):

    """ Logs a message to the LogService """
    lm = LogMessage((Request(logType, message)))
    self.bus.receive(lm)
