from lib import padConfig, padTUI

class Menu:
  def __init__(self, config, tui):
    self.config = config.config
    self.tui = tui

## MAIN
  optionsMain = {
    1: 'Select Wordlist',
    2: 'Build Values',
    3: 'Build Phrases',
    4: 'View Settings'
  }

  def menuMain(self):
    option = self.tui.prompt(self.optionsMain)
    self.actionsMain(option)

  def actionsMain(self, option):
    print('Returned', option)
    exit()

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