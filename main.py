from lib import PassGrid_Config, PassGrid_TUI, PassGrid_Menus

def main():
  config = PassGrid_Config.PassGrid_Config()
  tui = PassGrid_TUI.PassGrid_TUI()
  menu = PassGrid_Menus.PassGrid_Menus(config, tui)
  msg = config.init_config()

  while(True):
    menu.menu_main(msg)

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    try:
      exit()
    except SystemExit:
      exit()

