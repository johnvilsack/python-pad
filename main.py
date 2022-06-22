from lib import padConfig, padTUI, padMenus

config = padConfig.Config()
tui = padTUI.TUI(config)
menu = padMenus.Menu(config, tui)

default = {
  'config': 'settings.ini',
  'listsdir': './data',
  'wordfile': 'wordle-answers.json',
  'gridcols': '10',
  'gridrows': '10' 
}

def main():
  config.initConfig(default)
  while(True):
    menu.menuMain()
    exit()

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    try:
      exit()
    except SystemExit:
      exit()
