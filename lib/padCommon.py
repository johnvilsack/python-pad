class Common:
  def __init__(self):
    print('Loaded')

  def listDataFiles(self):
    i = 1
    for filename in self.defaultDataFiles:
      stri = str(i)
      self.config['DATAFILES'][stri] = filename
      i = i+1
    return self.config['DATAFILES']