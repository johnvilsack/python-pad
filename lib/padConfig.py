import os, uuid, configparser

class Config:
  def __init__(self):
    self.config = configparser.ConfigParser()
    self.defaultDataFiles = os.listdir('./data')
    self.wordlist = []

  def loadConfigFile(self, file):
    self.config.read(file)

  def saveConfigFile(self, file):
    with open(file, 'w') as fileConfig:
      self.config.write(fileConfig)
    print('Config saved.')

  def defaultConfigSettings(self):
    self.randomseed = uuid.uuid1().hex
    self.config['SETTINGS'] = {
      'WORDFILE' : '2k-common-words.csv',
      'GRIDCOLS' : '26',
      'GRIDSEED' : self.randomseed,
      'NUMTOGEN' : '25',
      'XPOPRATE' : '65535'
    }

  def saveMenu(self):
    fileName = input('Save config as %s?\nReturn to accept or enter new name: ' % self.config['INTERNAL']['currentConfigFile'])
    if (fileName == ''):
      fileName = self.config['INTERNAL']['currentConfigFile']
    self.saveConfigFile(fileName)

  def listDataFiles(self):
    i = 1
    for filename in self.defaultDataFiles:
      stri = str(i)
      self.config['DATAFILES'][stri] = filename
      i = i+1
    return self.config['DATAFILES']

  # def loadWordFile(self):
  #   file = self.config['DATAFILES'][option]
  #   with open(file) as f:
  #     self.wordlist = [line.rstrip() for line in f]