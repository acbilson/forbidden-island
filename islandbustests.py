import unittest
from islandservice import *
from islandbus import *
from constants import *
from message import *

class TestIslandBus(unittest.TestCase):

  bus = None

  def setUp(self):
    self.bus = IslandBus()

  def test_ctor(self):
    bus = IslandBus()

  # When the bus sends a message that all should receive, they receive it
  def test_send_broadcastAllSubscibers(self):
    serviceForSome = TestService_MoveMessages(self.bus)
    serviceForAll = TestService_AllMessages(self.bus)
    subscribers = [serviceForSome, serviceForAll]
    message = MoveMessage("Test move message")

    self.bus.send(message)

    self.assertEqual(2, len(self.bus.subscribers))
    self.assertTrue(serviceForAll.wasCalled)
    self.assertTrue(serviceForSome.wasCalled)

  # When the bus sends a message that only some should receive, some receive it
  def test_send_specificSubscribers(self):
    serviceForSome = TestService_MoveMessages(self.bus)
    serviceForAll = TestService_AllMessages(self.bus)
    subscribers = [serviceForSome, serviceForAll]
    message = ScreenMessage("Test screen message")

    self.bus.send(message)

    self.assertEqual(2, len(self.bus.subscribers))
    self.assertTrue(serviceForAll.wasCalled)
    self.assertFalse(serviceForSome.wasCalled)

  def test_receive_addsToQueue(self):
    message = MoveMessage("Test move message")
    self.bus.receive(message)

    self.assertFalse(self.bus.messageQueue.empty())
    receivedMessage = self.bus.messageQueue.get()
    self.assertTrue(message == receivedMessage)

  # When the bus listens, should send all messages in the queue
  def test_listen_sendsAllMessages(self):
    m1 = MoveMessage("First Message")
    m2 = MoveMessage("Second Message")
    m3 = MoveMessage("Third Message")
    self.bus.receive(m1)
    self.bus.receive(m2)
    self.bus.receive(m3)
    service = TestService_MoveMessages(self.bus)

    self.bus.listen()

    self.assertTrue(service.wasCalled)
    self.assertEqual(3, service.callNumber)
    self.assertTrue(self.bus.messageQueue.empty())

class TestService_AllMessages(IslandNotifier):
  
  def __init__(self, bus):
    IslandNotifier.__init__(self, bus)
    self.subscribedMessages.append(MessageType.All)
    self.wasCalled = False
 
  def on_next(self, message):
    self.wasCalled = True

class TestService_MoveMessages(IslandNotifier):
  
  def __init__(self, bus):
    IslandNotifier.__init__(self, bus)
    self.subscribedMessages.append(MessageType.Console_Move)
    self.wasCalled = False
    self.callNumber = 0
   
  def on_next(self, message):
    self.wasCalled = True
    self.callNumber = self.callNumber + 1
