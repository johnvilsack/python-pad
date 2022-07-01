import os

class PassGrid_TUI:
  def __init__(self):
    self.color = {
      'fg_black': '\u001b[30m',
      'fg_red': '\u001b[31m',
      'fg_green': '\u001b[32m',
      'fg_yellow': '\u001b[33m',
      'fg_blue': '\u001b[34m',
      'fg_magenta': '\u001b[35m',
      'fg_cyan': '\u001b[36m',
      'fg_white': '\u001b[37m',
      'bg_black': '\u001b[40m',
      'bg_red': '\u001b[41m',
      'bg_green': '\u001b[42m',
      'bg_yellow': '\u001b[43m',
      'bg_blue': '\u001b[44m',
      'bg_magenta': '\u001b[45m',
      'bg_cyan': '\u001b[46m',
      'bg_white': '\u001b[47m',      
      'style': {
        'bold': '\u001b[1m',
        'underline': '\u001b[4m',
        'reverse': '\u001b[7m',
        'reset': '\u001b[0m',
        'bright': ';1'
      }
    }
     
  def clear(self):
    os.system('cls||clear')
  
  def displayMenu(self, options, msg=None):
    self.clear()
    for key in options.keys():
      self.opt(key, options[key])
    self.opt('S', 'Save')
    self.opt('Q', 'Quit')
    if msg is not None:
      print('\n', msg, '\n')

  def opt(self, key, value):
    print('[{0}] {1}'.format(key, value))
    return
  
  def prompt(self, options, config, msg=None):

    self.displayMenu(options, msg)

    option = input('\nEnter Option > ')

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
    self.clear()
    print('Exiting Passpad')
    quit()