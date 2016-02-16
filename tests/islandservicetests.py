import unittest
import sys
sys.path.append('../src')
from island import *
from islandbus import *
from service_island import *
from constants import *
from message import *
from cards import *
import sys
from iofactory import *

class TestIslandNotifier(unittest.TestCase):

  notifier = None

  def setUp(self):
    bus = IslandBus()
    self.notifier = IslandNotifier(bus)

  def test_ctor(self):
    bus = IslandBus()
    notifier = IslandNotifier(bus)

  def test_notify(self):
    msg = TestMessage(Request("Up"))
    self.notifier.notify(msg)

    self.assertFalse(self.notifier.bus.messageQueue.empty())
    receivedMsg = self.notifier.bus.messageQueue.get()
    self.assertEqual("Up", receivedMsg.request.header)

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

# Message for these tests
class TestMessage(IslandMessage):

  def __init__(self, request):
    IslandMessage.__init__(self, MessageType.Test, request)
