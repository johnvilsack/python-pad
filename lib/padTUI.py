import os
from lib import padConfig

class TUI:
  def __init__(self, config):
    self.config = config
    
  # Simple clear for TUI
  def clear(self):
    os.system('cls||clear')
  
  def displayMenu(self, options):
    for key in options.keys():
      print('\t', key, options[key])
  
  def displayAnyKey(self):
    input('\nPress Any Key to Continue...')
    TUI.clear(self)

  def prompt(self, options):
    self.displayMenu(options)
    option = input('\nChoose #, [q] to quit: ')
    if not option.isdigit():
      if (option == 'q'):
        self.exitPassPad()
      elif (option == 's'):
        ## How to pass save data???
        self.config.saveMenu()
        self.prompt(options)
      else:
        print('Illegal Value')
        self.displayAnyKey()
        self.prompt(options)
    else:
      return option
      
  def exitPassPad(self):
    TUI.clear(self)
    print('Exiting Passpad')
    quit()