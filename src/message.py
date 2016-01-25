from enum import Enum

class MessageFactory(object):

  def __init__(self):
    self.moveContent = ['Up', 'Down', 'Left', 'Right']
  
  def get_message(self, content):
    if content in self.moveContent:
      return ConsoleMessage()
    else:
      return BroadcastMessage()

class IslandMessage(object):

  """ Base message class """

  def __init__(self, content, msgType):
    self.content = content
    self.type = msgType

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
    IslandMessage.__init__(self, content, MessageType.Screen_Refresh)

class PlayerMessage(IslandMessage):

  def __init__(self, content):
    IslandMessage.__init__(self, content, MessageType.Player)

class LogMessage(IslandMessage):
  
  def __init__(self, content):
    IslandMessage.__init__(self, content, MessageType.Log)

class StartMessage(IslandMessage):

  def __init__(self):
    IslandMessage.__init__(self, "Starting...", MessageType.Initialize)

class Response(object):
  
  def __init__(self, success, message=None):
    self.success = success
    self.message = message

  def __str__(self):
    return "R( success: " + self.success + " : " + self.message + ")"

  def __repr__(self):
    return __str__()

class MessageType(Enum):
  All = 0
  Initialize = 1
  Console = 2
  Console_Move = 3
  Screen_Refresh = 4
  Player = 5
  Log = 9

