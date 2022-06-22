import os, sys, uuid, configparser

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
    print('Initializing...')
    if len(sys.argv) > 1:
      iconfig = sys.argv[1]
      print('Argument detected. Attempting to load config:', iconfig)
    elif os.path.exists(default['config']):
      print('Loading previous or default settings')
      iconfig = default['config']
    else:
      self.defaultConfigSettings(default)
      iconfig = default['config']
    self.loadConfigFile(iconfig)
    if not self.config.has_section('SETTINGS'):
      print(iconfig, 'not found or invalid')
      exit()

  def loadConfigFile(self, file):
    self.config.read(file)

  def saveConfigFile(self, file):
    with open(file, 'w') as f:
      self.config.write(f)
    f.close()
    print('Config written to', file)
    return

  def saveMenu(self):
    fileName = input('Save config as %s?\nReturn to accept or enter new name: ' % self.config['SETTINGS']['config'])
    if (fileName == ''):
      fileName = self.config['SETTINGS']['config']
    file, ext = os.path.splitext(fileName)
    if not ext:
      ext = '.ini'
    fileName = file + ext
    self.saveConfigFile(fileName)