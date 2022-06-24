from lib import padConfig, padTUI, padMenus

def main():
  config = padConfig.Config()
  tui = padTUI.TUI()
  menu = padMenus.Menu(config, tui)
  msg = config.init_config()

  while(True):
    menu.menuMain(msg)

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    try:
      exit()
    except SystemExit:
      exit()
