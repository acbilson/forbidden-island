from constants import * 

class MessageFactory(object):

  def __init__(self):
    self.consoleContent = ['Up', 'Down', 'Left', 'Right']
  
  def get_message(self, content):
    if content in self.consoleContent:
      return ConsoleMessage()

      return IslandMessage()


class IslandMessage(object):

  def __init__(self, content, msgType):
    self.content = content
    self.type = msgType

class ConsoleMessage(IslandMessage):

  def __init__(self, content, msgType):
    IslandMessage.__init__(self, content, msgType)
  
