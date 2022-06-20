import os, sys
from lib import padConfig, padMenus, padTUI

tui = padTUI.TUI()
menu = padMenus.Menu()
config = padConfig.Config()

## Editable values
defaultConfigFile = 'settings.ini'
currentConfigFile = 'settings.ini'
#! 

config.config['RUNTIME'] = {
  'defaultConfigFile' : defaultConfigFile,
  'currentConfigFile' : currentConfigFile
}

## CONFIG LOADER
def loadSettings(defaultConfigFile, currentConfigFile, config):
  tui.clear()
  if len(sys.argv) > 1:
    print('Loading custom config...')
    currentConfigFile = sys.argv[1]
    config.loadConfigFile(currentConfigFile)
    if not config.config.has_section('SETTINGS'):
      print(currentConfigFile, 'Not Found or Contains Errors')
      tui.displayAnyKey()
      tui.exitPassPad()
  elif os.path.exists(defaultConfigFile):
    print('Loading existing settings at settings.ini...')
    config.loadConfigFile(defaultConfigFile)
  else:
    print('Starting Fresh')
  print('\n')
  return config
#!


# def menuBuildGrid():
#   tui.clear()
#   tui.displayMenu(config.listDataFiles())
#   option = tui.prompt(config)
#   config.loadWordFile(option)
#   for values in config.wordlist:
#     print(values)
#   tui.prompt(config)











def main():
  loadSettings(defaultConfigFile, currentConfigFile, config)
  while(True):
    tui.displayMenu(menu.optionsMain())
    option = tui.prompt(config)
    menu.actionsMain(config, tui, option)

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    try:
      tui.exitPassPad()
    except SystemExit:
      tui.exitPassPad()
