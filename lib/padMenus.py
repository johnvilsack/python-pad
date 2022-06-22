from lib import padConfig, padTUI

class Menu:
  def __init__(self, config, tui):
    self.config = config.config
    self.tui = tui

  ## MAIN
  def menuMain(self, msg=None):
    options = {
      1: 'Make A Passpad'
    }
    self.actionsMain(self.tui.prompt(options, msg))

  def actionsMain(self, option):
    match option:
      case '1':
        self.menuNewPasspad()
        return
      case _:
        msg = 'Unknown Value. Try again.'
        self.menuMain(msg)

  def menuNewPasspad(self, msg=None):
    options = {
      1: 'Use current settings',
      2: 'Use new settings wizard'
    }
    self.actionsNewPasspad(self.tui.prompt(options, msg))

  def actionsNewPasspad(self, option):
    match option:
      case '1':
        print('foo')
        return
      case _:
        msg = 'Unknown Value. Try again.'
        self.menuNewPasspad(msg)
















  # def actionsMain(self):
  #   option = int(option)
  #   if option in self.optionsMain().keys():
  #     tui.clear()
  #     match option:
  #       case 1:
  #         print('Select word file used to populate grid:\n')
  #         tui.displayMenu(self.optionsWordList(config, tui, option))
  #         option = tui.prompt(config)
  #         self.actionsWordList(config, tui, option)
  #         return
  #       case 2:
  #         print('THREE')
  #         return
  #   else:
  #     print('Unknown Value')
  #     return


    # self.actionsMain(padConfig, padTUI, option)

## WORDLIST
  # def optionsWordList(self, config, tui, option):
  #   settingsWordFileText = '\t[Currently Selected] ' + config.config['SETTINGS']['wordfile'] + '\n'
  #   print(settingsWordFileText)
  #   options = config.listDataFiles()
  #   return options
  
  # def actionsWordList(self, config, tui, option):
  #   if (config.config.has_option('DATAFILES', option)):
  #     newWordList = config.config.get('DATAFILES', option)
  #     config.config.set('SETTINGS','WORDFILE', newWordList)
  #     print('New File Selected')
  #     return
  #   else:
  #     print('Keeping Existing')
  #     return
  
  # def saveMenu(self):
  #   fileName = input('Save config as %s?\nReturn to accept or enter new name: ' % self.config['INTERNAL']['currentConfigFile'])
  #   if (fileName == ''):
  #     fileName = self.config['INTERNAL']['currentConfigFile']
  #   self.saveConfigFile(fileName)