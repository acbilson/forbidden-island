import unittest
import sys
sys.path.append('..\src')
from island import *
from islandbus import *
from islandservice import *
from consoleservice import *
from playerservice import *
from screenservice import *
from logservice import *
from constants import *
from message import *
import sys
sys.path.append('C:\SourceCode\PersonalRepo\Python\PyLexLib')
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

class TestConsoleService(unittest.TestCase):

  cs = None
  fio = None

  def setUp(self):
    bus = IslandBus()
    fio = FakeIO()
    self.cs = ConsoleService(bus, self.fio)

  def test_ctor(self):
    bus = IslandBus()
    fio = FakeIO()
    cs = ConsoleService(bus, fio)

  def test_on_message_received_notHandled(self):
    msg = ScreenMessage(Request("Test screen message"))
    self.cs.on_message_received(msg)

class TestPlayerService(unittest.TestCase):

  ps = None

  def setUp(self):
    bus = IslandBus()
    self.ps = PlayerService(bus)

  def test_ctor(self):
    bus = IslandBus()
    ps = PlayerService(bus)

  # TODO: Fix test
  # def test_on_message_received_emptyMessage_nothingHappens(self):

    # """ When a message is received, if it is not handled by this service, None is returned """

    # msg = PlayerMessage("")
    # actual = self.ps.on_message_received(msg)

    # self.assertIsNone(actual)

class TestScreenService(unittest.TestCase):

  ss = None
  fio = None

  def setUp(self):
    bus = IslandBus()
    island = Island()
    self.fio = FakeIO()
    self.ss = ScreenService(bus, island, self.fio)

  def test_ctor(self):
    bus = IslandBus()
    island = Island()
    fio = FakeIO()
    ss = ScreenService(bus, island, fio)

  def test_on_message_received_emptyMessage_nothingHappens(self):

    """ When a message is received, if it is not handled by this service, None is returned """

    msg = ScreenMessage(Request(""))
    actual = self.ss.on_message_received(msg)

    self.assertIsNone(actual)

  def test_on_message_received_initialize_starts(self):
    msg = ConsoleMessage(Request("Initialize"))
    actual = self.ss.on_message_received(msg)


  def test_on_message_received_render_printsBoard(self):
    msg = ScreenMessage(Request("Render"))
    actual = self.ss.on_message_received(msg)

# Message for these tests

class TestMessage(IslandMessage):

  def __init__(self, request):
    IslandMessage.__init__(self, MessageType.Test, request)
