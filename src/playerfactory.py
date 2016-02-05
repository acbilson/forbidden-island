from constants import *
from player import *
from player_diver import *
from player_engineer import *
from player_explorer import *
from player_messenger import *
from player_navigator import *
from player_pilot import *

class PlayerFactory(object):

  def __init__(self):
    self.playerCommands = self._get_commands()

  def get_diver(self):

    diver = DiverPlayer(self.playerCommands)
    return diver

  def get_engineer(self):

    engineer = EngineerPlayer(self.playerCommands)
    return engineer

  def get_pilot(self):

    pilot = PilotPlayer(self.playerCommands)
    return pilot

  def get_navigator(self):

    navigator = NavigatorPlayer(self.playerCommands)
    return navigator

  def get_messenger(self):

    messenger = MessengerPlayer(self.playerCommands)
    return messenger

  def get_explorer(self):

    explorer = ExplorerPlayer(self.playerCommands)
    return explorer

  def get_instance(self, playerType):

    options = {
      Constant.PlayerType["Diver"]: self.get_diver,
      Constant.PlayerType["Engineer"]: self.get_engineer,
      Constant.PlayerType["Pilot"]: self.get_pilot,
      Constant.PlayerType["Navigator"]: self.get_navigator,
      Constant.PlayerType["Messenger"]: self.get_messenger,
      Constant.PlayerType["Explorer"]: self.get_explorer
    }

    execute = options.get(playerType, "nothing")
    player = execute()
    return player

  def _get_commands(self):
    commands = [MoveCommand(PlayerMover())]
    return commands
