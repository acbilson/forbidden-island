import json
from enum import Enum

class MessageFactory(object):

  def __init__(self):
    self.moveContent = ['Up', 'Down', 'Left', 'Right']
  
  def get_message(self, content):
    if content in self.moveContent:
      return ConsoleMessage()
    else:
      return BroadcastMessage()

# TODO: Consolidate messages; there are more than I need or use.
class IslandMessage(object):

  """ Base message class """

  def __init__(self, content, msgType):
    self.content = content
    self.type = msgType

  def __str__(self):
    return "M(" + str(self.type.value) + "," + str(self.content) + ")"

  def __repr__(self):
    return self.__str__()

class BroadcastMessage(IslandMessage):
  
  def __init__(self, content):
    IslandMessage.__init__(self, content, MessageType.All)

class MoveMessage(IslandMessage):

  def __init__(self, content):
    IslandMessage.__init__(self, content, MessageType.Console_Move)

class ConsoleMessage(IslandMessage):

  def __init__(self, content):
    IslandMessage.__init__(self, content, MessageType.Console)

class ScreenMessage(IslandMessage):

  def __init__(self, content):
    IslandMessage.__init__(self, content, MessageType.Screen)

class PlayerMessage(IslandMessage):

  def __init__(self, content):
    IslandMessage.__init__(self, content, MessageType.Player)

class LogMessage(IslandMessage):
  
  def __init__(self, content):
    IslandMessage.__init__(self, content, MessageType.Log)

class StartMessage(IslandMessage):

  def __init__(self):
    IslandMessage.__init__(self, "Starting...", MessageType.Initialize)

class ExitMessage(IslandMessage):

  def __init__(self):
    IslandMessage.__init__(self, "Exiting...", MessageType.Exit)

class Request(object):

  def __init__(self, header, content):
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
