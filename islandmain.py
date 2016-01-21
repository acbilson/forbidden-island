import sys
sys.path.append('C:\SourceCode\PersonalRepo\Python\PyLexLib')
from iofactory import *

class IslandGame(object):
  """ Central class for the Forbidden Island game, where the game loop executes """

  def __init__(self, notifier, messageFactory):
    self.notifier = notifier
    self.messageFactory = messageFactory

  def play(self):
    self.notifier.send(ScreenMessage("Start"))
    while(true):
      break
  
