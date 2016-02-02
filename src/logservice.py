from islandservice import *

class LogService(IslandSubscriber):
  
  def __init__(self, bus, io):
    IslandNotifier.__init__(self, bus)
    self.io = io
    self.subscribedMessages.append(MessageType.All)
    self.subscribedMessages.append(MessageType.Log)
    self.log = []

  def on_message_received(self, message):
    entry = message.type.name + " Content: " + str(message.request) + '\n'
    self.log.append(entry)

  def print_all(self):
    print("\nDebug Report:")
    for i,l in enumerate(self.log):
      report = str(i) + ": " + l
      self.io.write(report)

