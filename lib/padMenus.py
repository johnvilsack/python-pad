from lib import padConfig, padMenus, padTUI

class Menu:

## MAIN
  def optionsMain(self):
    options = {
      1: 'Choose Word List',
      2: 'Build Values',
      3: 'Build Phrases',
      4: 'View Settings'
    }
    return options

  def actionsMain(self, config, tui, option):
    option = int(option)
    if option in self.optionsMain().keys():
      tui.clear()
      match option:
        case 1:
          print('Select word file used to populate grid:\n')
          tui.displayMenu(self.optionsWordList(config, tui, option))
          option = tui.prompt(config)
          self.actionsWordList(config, tui, option)
          return
        case 2:
          print('TWO')
          return
        case 3:
          print('THREE')
          return
        case 4:
          print('FOUR')
          return
    else:
      print('Unknown Value')
      return

## WORDGRID
  def optionsWordList(self, config, tui, option):
    settingsWordFileText = '\t[Currently Selected] ' + config.config['SETTINGS']['wordfile'] + '\n'
    print(settingsWordFileText)
    options = config.listDataFiles()
    return options
  
  def actionsWordList(self, config, tui, option):
    if (config.config.has_option('DATAFILES', option)):
      newWordList = config.config.get('DATAFILES', option)
      config.config.set('SETTINGS','WORDFILE', newWordList)
      print('New File Selected')
      return
    else:
      print('Keeping Existing')