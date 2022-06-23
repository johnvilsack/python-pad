from lib import padConfig, padTUI, padMenus

def main():
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

  msg = config.initConfig(default)
  while(True):
    menu.menuMain(msg)
    exit()

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    try:
      exit()
    except SystemExit:
      exit()
