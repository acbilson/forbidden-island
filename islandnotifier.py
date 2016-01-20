from constants import * 

class IslandNotifier(object):

  EXIT_CODE = 'Q'

  def __init__(self):
    self.subscribers = []

  def notify(self, message):
    """ Sends a message to the appropriate subscribers for that message type """
    pass

  def subscribe(self, subscriber, messageTypes=MessageType.All):
    """ Adds a subscriber to the list which will be notified 
    for the specified message types, or all if none specified """
    pass

  def _get_subscribers_to_notify(self, messageType):
    """ Returns all subscribers that will be notified for this message type """
    pass

  def _has_exited(self, input):
    pass

class IslandMessage(object):

  def __init__(self):
    pass

class ConsoleMessage(IslandMessage):

  def __init__(self):
    super.__init__()
    pass
  
