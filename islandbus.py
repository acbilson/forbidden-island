from queue import Queue
from constants import * 
from message import *
from islandservice import *

class IslandBus(object):

  def __init__(self):
    self.subscribers = []
    self.messageQueue = Queue()

  def listen(self):
    """ loops through the message queue, sending messages to the appropriate subscribers """
    while not self.messageQueue.empty():
    
      message = self.messageQueue.get()
      self.send(message)

  def send(self, message):
    """ Sends a message to the appropriate subscribers for that message type """
    subscribers = self._get_subscribers_to_notify(message)

    for s in subscribers:
      s.on_message_received(message)

  def receive(self, message):

    """ Receives a message and adds it to a queue that will be used to notify other subscribers """

    self.messageQueue.put(message)

  def add_subscriber(self, subscriber):

    """ Adds a subscriber to the list which will be notified 
    for its specified message types, or all if none specified """

    self.subscribers.append(subscriber)

  def _get_subscribers_to_notify(self, message):

    """ Returns all subscribers that will be notified for this message type """
    
    notifiedSubscribers = []

    for s in self.subscribers:
      # disclude log from all so that I can send to log only
      if MessageType.All in s.subscribedMessages and message.type != MessageType.Log:
        notifiedSubscribers.append(s)
      if message.type in s.subscribedMessages:
        notifiedSubscribers.append(s)

    return notifiedSubscribers
