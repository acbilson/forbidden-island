class Page(object):

  def __init__(self):
    self.values = [3,6,9,12,15,18,21,24,27,30]

class Position(object):

  def __init__(self, index=0, value=0):
    self.index = index
    self.value = value

#Invoker
class Player(object):
  
  def __init__(self):
    self.page = Page()
    self.commandHistory = []
    self.currentPosition = Position(3, self.page.values[3])

  def move(self, moveType):
    move = Move(self.currentPosition, moveType, self.page)
    move.execute()
    self.commandHistory.append(move)

  def undo(self):
    lastCommand = self.commandHistory.pop()
    lastCommand.unexecute()

#Command
class Move(object):

  def __init__(self, position, moveType, page):
    self.page = page
    self.position = position
    self.moveType = moveType

  def execute(self):

    if self.moveType == MoveType.Left:
      self.position.value = self.page.values[self.position.index - 1]
    elif self.moveType == MoveType.Right:
      self.position.value = self.page.values[self.position.index + 1]

  def unexecute(self):

    if self.moveType == MoveType.Left:
        self.position.value = self.page.values[self.position.index + 1]
    elif self.moveType == MoveType.Right:
      self.position.value = self.page.values[self.position.index - 1]
      
class MoveType():

  Left = "Left"
  Right = "Right"

if __name__ == "__main__":


  p = Player()
  print("Started at: " + str(p.currentPosition.value))
  p.move(MoveType.Left)
  print("Moved left")
  print("Ended at: " + str(p.currentPosition.value))
  print("Moved right")
  p.move(MoveType.Right)
  print("Moved right")
  p.move(MoveType.Right)
  print("Ended at: " + str(p.currentPosition.value))
  print("Undid last")
  p.undo()
  print("Ended at: " + str(p.currentPosition.value))
