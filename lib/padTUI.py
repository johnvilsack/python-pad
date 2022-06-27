import os, configparser

class TUI:
  def __init__(self):
    print('TUI loaded')
     
  def clear(self):
    print('Clear Attempt')
    #os.system('cls||clear')
  
  def displayMenu(self, options, msg=None):
    self.clear()
    self.line()
    for key in options.keys():
      self.opt(key, options[key])
    self.line()
    if msg is not None:
      print('\n', msg, '\n')

  def opt(self, key, value):
    print('\t[{0}] {1}'.format(key, value))
    return
  
  def line(self):
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    return
  def prompt(self, options, config, msg=None):

    self.displayMenu(options, msg)

    option = input('\n[S]ave [Q]uit Enter Option >>> ')

    if not option.isdigit():
      option = option.lower()
      if (option == 'q'):
        self.exitPassPad()
      elif (option == 's'):
        msg = config.display_save_menu()
        print(msg)
        self.prompt(options, config, msg)
    else:
      return option
      
  def exitPassPad(self):
    TUI.clear(self)
    print('Exiting Passpad')
    quit()