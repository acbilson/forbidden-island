# from collections import deque
from queue import Queue
from constants import * 
from message import *

class IslandNotifier(object):

  """ Mixin class to send messages to an instance of the IslandBus """
  def __init__(self):
    pass

class IslandSubscriber(object):

  """ Mixin class to subscribe to messages from the IslandBus """

  def __init__(self):
    self.lastMessage = None
    self.subscribedMessages = []

  def subscribe(self, notifier):
    """ Adds this subscriber to this notifier's list """
    pass

  def on_next(self, message):
    """ Event the notifier will raise when a message applies to this subscriber """
    pass
