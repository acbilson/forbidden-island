# from collections import deque
from queue import Queue
from constants import * 
from message import *

class IslandBus(object):

  EXIT_CODE = 'Q'

  def __init__(self):
    self.subscribers = []
    self.messageQueue = Queue([])

  def listen(self):
    """ loops through the message queue, sending messages to the appropriate subscribers """
    while self.messageQueue.full():
    
      message = self.messageQueue.get()
      self.send(message)

  def send(self, message):
    """ Sends a message to the appropriate subscribers for that message type """
    subscribers = self._get_subscribers_to_notify()

    for s in subscribers:
      s.on_next(message)

  def receive(self, message):
    """ Receives a message and adds it to a queue that will be used to notify other subscribers """
    self.messageQueue.push(message)

  def add_subscriber(self, subscriber):
    """ Adds a subscriber to the list which will be notified 
    for its specified message types, or all if none specified """
    self.subscribers.append(subscriber)

  def _get_subscribers_to_notify(self, messageType):
    """ Returns all subscribers that will be notified for this message type """
    return [s for s in self.subscribers if messageType in s.subscribedMessages]
