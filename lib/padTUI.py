import os
from lib import padConfig, padMenus, padTUI

class TUI:
  # Simple clear for TUI
  def clear(self):
    os.system('cls||clear')
  
  def displayMenu(self, menu):
    for key in menu.keys():
      print('\t', key, menu[key])
  
  def displayAnyKey(self):
    input('\nPress Any Key to Continue...')
    TUI.clear(self)

  def prompt(self, config):
    option = input('\nChoose #, [q] to quit: ')
    if not option.isdigit():
      if (option == 'q'):
        self.exitPassPad()
      elif (option == 's'):
        config.saveMenu()
      else:
        print('Illegal Value')
        self.displayAnyKey()
        # HOW TO GO BACK?
    return option
      
  def exitPassPad(self):
    TUI.clear(self)
    print('Exiting Passpad')
    quit()