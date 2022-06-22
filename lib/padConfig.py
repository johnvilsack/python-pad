import os, sys, uuid, configparser, shutil, time

class Config:
  def __init__(self):
    self.config = configparser.ConfigParser()
    self.wordlist = []

  def defaultConfigSettings(self, default):
    self.randomseed = uuid.uuid1().hex
    self.config['SETTINGS'] = {
      'gridseed' : self.randomseed,
    }
    self.config['SETTINGS'].update(default)
    self.saveConfigFile(default['config'])
    print('Creating new default settings file')
    return

  def initConfig(self, default):
    if len(sys.argv) > 1:
      iconfig = sys.argv[1]
      msg = 'Argument detected. Attempting to load config:' + iconfig
    elif os.path.exists(default['config']):
      msg = 'Loading previous or default settings'
      iconfig = default['config']
    else:
      self.defaultConfigSettings(default)
      iconfig = default['config']
    self.loadConfigFile(iconfig)
    if not self.config.has_section('SETTINGS'):
      print(iconfig, 'not found or invalid')
      exit()
    return msg

  def loadConfigFile(self, file):
    self.config.read(file)

  def saveConfigFile(self, file):
    self.config['SETTINGS']['config'] = file
    if os.path.exists(file):
      shutil.copyfile(file, './settings_backup/BACKUP-' + str(time.strftime('%d%m%y-%H%M%S', time.gmtime())) + '-' + file)
    with open(file, 'w') as f:
      self.config.write(f)
    f.close()
    msg = 'Saved ' + file + ' and set file as current config'
    return msg

  def saveMenu(self):
    fileName = input('Enter file name or save as [%s]: ' % self.config['SETTINGS']['config'])
    if (fileName == ''):
      fileName = self.config['SETTINGS']['config']
    file, ext = os.path.splitext(fileName)
    if not ext:
      ext = '.ini'
    fileName = file + ext
    msg = self.saveConfigFile(fileName)
    return msg