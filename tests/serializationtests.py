import unittest
import sys
sys.path.append('..\src')
from constants import *
from serialization import *

class TestMessageSerialization(unittest.TestCase):

  def test_messageEncoder_encodesMessageToJSON(self):

    message = ConsoleMessage("Test Message")
    actual = json.dumps(message, cls=MessageEncoder, sort_keys=True)
    
    expected = '{"__IslandMessage__": true, "content": "Test Message", "type": ' + str(MessageType.Console.value) + '}'
    self.assertEqual(expected, actual)

  def test_messageDecoder_decodesMessageFromJSON(self):

    jsonMessage = '{"__IslandMessage__": true, "content": "Test Message", "type": ' + str(MessageType.Console.value) + '}'

    decoder = MessageDecoder()
    actual = json.loads(jsonMessage, object_hook=decoder.as_island_message)

    self.assertEqual("Test Message", actual.content)
    self.assertEqual(ConsoleMessage, type(actual))
    self.assertEqual(MessageType.Console, actual.type)

class TestPlayerSerialization(unittest.TestCase):

  def test_playerEncoder_encodesMessageToJSON(self):

    player = Player(PlayerType.Pilot)
    actual = json.dumps(player, cls=PlayerEncoder, sort_keys=True)
    
    expected = '{"__Player__": true, "type": "PLT"}'
    self.assertEqual(expected, actual)

  def test_playerDecoder_decodesMessageFromJSON(self):

    jsonPlayer = '{"__Player__": true, "type": "' + PlayerType.Pilot + '"}'

    decoder = PlayerDecoder()
    actual = json.loads(jsonPlayer, object_hook=decoder.as_player)

    self.assertEqual(Player, type(actual))

class TestRequestSerialization(unittest.TestCase):

  def test_requestEncoder_encodesMessageToJSON(self):

    request = Request("Create", { "type": "Diver"})
    actual = json.dumps(request, cls=RequestEncoder, sort_keys=True)
    
    expected = '{"__Request__": true, "content": "{\\"type\\": \\"Diver\\"}", "header": "Create"}'
    self.assertEqual(expected, actual)

  def test_requestDecoder_decodesMessageFromJSON(self):

    jsonRequest = '{"__Request__": true, "header": "Create", "content": "{ \\"type\\": \\"Diver\\" }" }'

    decoder = RequestDecoder()
    actual = json.loads(jsonRequest, object_hook=decoder.as_request)

    self.assertEqual(Request, type(actual))

