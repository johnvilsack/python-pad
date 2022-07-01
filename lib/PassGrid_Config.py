from datetime import datetime
import os, sys, uuid, configparser, shutil, time, string

class PassGrid_Config:
  def __init__(self):
    self.config = configparser.ConfigParser()

    # Create a generic seed from UUID to establish deterministic randomization
    self.default_section = 'SETTINGS'
    self.default_savesdir = './saves/' + datetime.now().strftime('%m-%d-%y_%H%M') + '/'
    self.default_options = {
      'conffile': 'settings.ini',
      'savesdir': self.default_savesdir,
      'listsdir': './data/',
      'wordfile': 'wordle-answers.json',
      'gridcols': '10',
      'gridrows': '10',
      'gridseed': str(uuid.uuid1().hex),
      'gridjson': 'grid.json',
      'colnames': string.ascii_uppercase
    }
  
  # Choose which config to load on initialization.
  def init_config(self):
    # Manual load via command line
    if len(sys.argv) > 1:
      # Check if file exists
      if os.path.exists(sys.argv[1]):
        iconfig = sys.argv[1]
        msg = '[FOUND] {0}'.format(iconfig)
      else:
        # Bomb out if not found. Chances are we were expecting a file.
        msg = '[FILE NOT FOUND] {0} \n **EXITING** '.format(sys.argv[1])
        print(msg)
        exit()
    # Autoloader
    else:
      # Check for default file
      if os.path.exists(self.default_options['conffile']):
        iconfig = self.default_options['conffile']
        msg = '[FOUND] {0}'.format(iconfig)
      else:
        iconfig = self.default_options['conffile']
        msg = '[NEW] Creating new {0}'.format(iconfig)
        msg += '\n' + self.set_default_config_settings()
      
    print(msg) 
    # Now that we've chosen our poison, let's load it up.
    msg = self.load_config_file(iconfig)

    print(msg)
    return msg

  # Sets defaults using configparser. This also behaves as a filesystem sanity check on first run.
  def set_default_config_settings(self):

    self.config.add_section(self.default_section)
    for k in self.default_options:
      self.config.set(self.default_section, k, self.default_options[k])

    self.save_config_file(self.config.get(self.default_section, 'conffile'))

    msg = '[OK] New config file created'
    return msg

  # Use configparser to load config
  def load_config_file(self, file):
    self.config.read(file)

    # Simple sanity check to see if it matches what we're expecting
    if not self.config.has_section(self.default_section):
      msg = '[ERROR] Config does not have section {0}'.format(self.default_section)
    else:
      msg = '[OK] {0} loaded'.format(file)
    return msg

  # Use configparse to save config
  def save_config_file(self, file):
    # Set that the entered name is now the file we'll be using
    self.config.set(self.default_section, 'conffile', file)

    # Automatically make a backup if there is already an existing file 
    if os.path.exists(file):
      shutil.copyfile(file, './settings_backup/BACKUP-' + str(time.strftime('%d%m%y-%H%M%S', time.gmtime())) + '-' + file)
    with open(file, 'w') as f:
      self.config.write(f)
    f.close()
    msg = '[SAVED] {0} and set as current working file'.format(file)
    return msg

  def display_save_menu(self):
    fileName = input('Enter file name or save as [%s]: ' % self.config['SETTINGS']['conffile'])
    if (fileName == ''):
      fileName = self.config['SETTINGS']['conffile']
    file, ext = os.path.splitext(fileName)
    if not ext:
      ext = '.ini'
    fileName = file + ext
    msg = self.save_config_file(fileName)
    return msg
  
if __name__ == "__main__":
  try:
    exit()
  except SystemExit:
    exit()