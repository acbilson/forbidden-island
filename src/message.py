import json
from enum import Enum

class MessageFactory(object):

  def __init__(self):
    self.moveContent = ['Up', 'Down', 'Left', 'Right']
  
  def get_message(self, request):
    if request in self.moveContent:
      return ConsoleMessage()
    else:
      return BroadcastMessage()

# TODO: Consolidate messages; there are more than I need or use.
class IslandMessage(object):

  """ Base message class """

  def __init__(self, msgType, request=None):
    self.request = request
    self.type = msgType

  def __str__(self):
    return "M(" + str(self.type.value) + "," + str(self.request) + ")"

  def __repr__(self):
    return self.__str__()

class MoveMessage(IslandMessage):

  def __init__(self, request):
    IslandMessage.__init__(self, MessageType.Console_Move, request)

class ConsoleMessage(IslandMessage):

  def __init__(self, request):
    IslandMessage.__init__(self, MessageType.Console, request)

class ScreenMessage(IslandMessage):

  def __init__(self, request):
    IslandMessage.__init__(self, MessageType.Screen, request)

class PlayerMessage(IslandMessage):

  def __init__(self, request):
    IslandMessage.__init__(self, MessageType.Player, request)

class LogMessage(IslandMessage):
  
  def __init__(self, request):
    IslandMessage.__init__(self, MessageType.Log, request)

class StartMessage(IslandMessage):

  def __init__(self):
    IslandMessage.__init__(self, MessageType.Initialize, Request("Starting..."))

class ExitMessage(IslandMessage):

  def __init__(self):
    IslandMessage.__init__(self, MessageType.Exit, Request("Exiting..."))

class Request(object):

  def __init__(self, header, content=None):
    self.header = header
    self.content = content

  def __str__(self):
    return "R(" + str(self.header) + "," + str(self.content) + ")"

  def __repr__(self):
    return self.__str___()

class MessageType(Enum):
  All = 0
  Initialize = 1
  Exit = 2
  Console = 3
  Screen = 4
  Player = 5
  Log = 9
  Test = 10
