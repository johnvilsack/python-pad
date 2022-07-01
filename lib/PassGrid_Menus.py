import PassGrid

class PassGrid_Menus:
  def __init__(self, config, tui):
    self.config = config
    self.tui = tui

  ## MAIN
  def menu_main(self, msg=None):
    options = {
      1: 'Make A Passpad'
    }
    self.actions_menu_main(self.tui.prompt(options, self.config, msg))

  def actions_menu_main(self, option):
    match option:
      case '1':
        self.menu_passgrid()
        return
      case _:
        msg = 'Unknown Value. Try again.'
        self.menu_main(msg)

  def menu_passgrid(self, msg=None):
    options = {
      1: 'Use current settings',
      2: 'Make Passcode'
    }
    self.actions_menu_passgrid(self.tui.prompt(options, self.config, msg))

  def actions_menu_passgrid(self, option):
    match option:
      case '1':
        passgrid = PassGrid.PassGrid(self.config)
        msg = passgrid.create_passgrid()
        self.menu_save_passgrid(passgrid, msg)
        return
      case '2':
        passgrid.randomPass()
        return
      case _:
        msg = 'Unknown Value. Try again.'
        self.menu_passgrid(msg)
  
  def menu_save_passgrid(self, passgrid, msg=None):
    options = {
      1: 'Save Passgrid to File',
    }
    self.actions_menu_save_passgrid(self.tui.prompt(options, self.config, msg), passgrid)
  
  def actions_menu_save_passgrid(self, option, passgrid, msg=None):
    match option:
      case '1':
        passgrid.save_passgrid()
        return
      case _:
        msg = 'Unknown Value. Try again.'
        self.menu_save_passgrid(msg)

if __name__ == "__main__":
  try:
    exit()
  except SystemExit:
    exit()