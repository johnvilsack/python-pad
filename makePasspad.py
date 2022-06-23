import string, itertools, random, json
from lib import padConfig, padTUI, padMenus

class WordList:
  def __init__(self, config):
    self.config = config.config
    self.WORDLIST = {}
  
  def openWordlist(self):
    with open(self.config['SETTINGS']['listsdir'] + self.config['SETTINGS']['wordfile'], 'r') as f:
      self.WORDLIST = json.load(f)
    return self.WORDLIST

  def makeAlphaColumns(self):
    GRIDCOLS = int(self.config['SETTINGS']['gridcols'])
    if (GRIDCOLS <= len(string.ascii_uppercase)):
      prod = itertools.product(string.ascii_uppercase)
    else:
      repeatcols = (GRIDCOLS // len(string.ascii_uppercase)) + 1
      prod = itertools.product(string.ascii_uppercase, repeat=repeatcols)
    result = []
    for values in prod:
      result.append(''.join(values))
    columns = []
    i = 0
    while i in range(GRIDCOLS):
      columns.append(result[i])
      i += 1
    return columns

  def randomizeWordList(self):
    GRIDSEED = self.config['SETTINGS']['gridseed']
    WORDLIST = self.WORDLIST
    random.seed(GRIDSEED)
    random.seed(random.getrandbits(128))
    random.shuffle(WORDLIST)
    return WORDLIST



def main():
  config = padConfig.Config()
  default = {
    'config': 'settings.ini',
    'listsdir': './data/',
    'wordfile': 'wordle-answers.json',
    'gridcols': '10',
    'gridrows': '10' 
  }
  config.initConfig(default)
  wordlist = WordList(config)
  actuallist = wordlist.openWordlist()
  COLUMNS = wordlist.makeAlphaColumns()
  RANDO = wordlist.randomizeWordList()
  print(RANDO)

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    try:
      exit()
    except SystemExit:
      exit()