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

class ScreenMessage(IslandMessage):

  def __init__(self, content):
    IslandMessage.__init__(self, content, MessageType.Screen_Refresh)

class StartMessage(IslandMessage):

  def __init__(self):
    IslandMessage.__init__(self, "Starting...", MessageType.Initialize)

class MessageType(Enum):
  All = 0
  Initialize = 1
  Console_Move = 2
  Screen_Refresh = 3

