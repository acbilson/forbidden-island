import json
from player import *
from message import *
class MessageEncoder(json.JSONEncoder):

  def default(self, obj):
    if isinstance(obj, IslandMessage):
      return {"__IslandMessage__": True, "content": obj.content, "type": obj.type.value}
    else:
      return json.JSONEncoder.default(self, obj)

class MessageDecoder():

  def as_island_message(self, dct):
    if '__IslandMessage__' in dct:
      message = self._get_by_message_type(dct)
      return message
    else:
      return dct;

  # TODO: Make into dictionary search for speed and clarity
  def _get_by_message_type(self, dct):
    msgType = dct.get("type")
    if msgType == MessageType.Console.value:
      return ConsoleMessage(dct['content'])
    elif msgType == MessageType.Initialize.value:
      return StartMessage(dct['content'])
    elif msgType == MessageType.Exit.value:
      return ExitMessage(dct['content'])
    elif msgType == MessageType.Log.value:
      return LogMessage(dct['content'])
    elif msgType == MessageType.Player.value:
      return PlayerMessage(dct['content'])
    else:
      return IslandMessage(dct['content'], MessageType.All)
      
class PlayerEncoder(json.JSONEncoder):

  def default(self, obj):
    if isinstance(obj, Player):
      player = {"__Player__": True, "type": obj.type }
      return player
    else:
      return json.JSONEncoder.default(self, obj)

class PlayerDecoder():

  def as_player(self, dct):
    if '__Player__' in dct:
      return Player(dct['type'])
    else:
      return dct;

class RequestEncoder(json.JSONEncoder):

  def default(self, obj):
    if isinstance(obj, Request):
      content = json.dumps(obj.content)
      player = {"__Request__": True, "header": obj.header, "content": content }
      return player
    else:
      return json.JSONEncoder.default(self, obj)

class RequestDecoder():

  def as_request(self, dct):
    if '__Request__' in dct:
      content = json.loads(dct['content'])
      return Request(dct['header'], content)
    else:
      return dct;
