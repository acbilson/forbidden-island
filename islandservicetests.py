import unittest
from islandbus import *
from islandservice import *
from constants import *
from message import *

class TestIslandNotifier(unittest.TestCase):

  notifier = None

  def setUp(self):
    bus = IslandBus()
    self.notifier = IslandNotifier(bus)

  def test_ctor(self):
    bus = IslandBus()
    notifier = IslandNotifier(bus)

  def test_notify(self):
    msg = MoveMessage("Up")
    self.notifier.notify(msg)

    self.assertFalse(self.notifier.bus.messageQueue.empty())
    receivedMsg = self.notifier.bus.messageQueue.get()
    self.assertEqual("Up", receivedMsg.content)

class TestIslandSubscriber(unittest.TestCase):

  subscriber = None

  def setUp(self):
    self.subscriber = IslandSubscriber()

  def test_ctor(self):
    subscriber = IslandSubscriber()
    self.assertEqual(0, len(subscriber.subscribedMessages))

  def test_subscribe(self):
    bus = IslandBus()
    self.subscriber.subscribe(bus)
    self.assertTrue(self.subscriber in bus.subscribers)

class TestConsoleService(unittest.TestCase):

  def test_ctor(self):
    bus = IslandBus()
    cs = ConsoleService(bus)
