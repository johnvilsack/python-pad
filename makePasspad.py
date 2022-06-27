import string, itertools, random, json
from lib import padConfig

class WordList:
  def __init__(self, config):
    self.config = config.config
    self.IMPORTED_WORDLIST = {}
    self.COLUMNS = {}
    self.RANDOMIZED_WORDLIST = {}
    self.GRID = {}
    self.TESTGRID = {}
  
  def generate_wordlist(self):
    # First, open the wordlist specified in config
    self.openWordlist()
    # Randomize this list based on gridseed
    self.randomizeWordList()
    # Make columns
    self.makeAlphaColumns()
    # Create actual Grid
    self.populateGrid()
    return

  # Open wordlist dictated in settings
  def openWordlist(self):
    with open(self.config['SETTINGS']['listsdir'] + self.config['SETTINGS']['wordfile'], 'r') as f:
      self.IMPORTED_WORDLIST = json.load(f)
    return

  # Convert gridcols integer in settings to alphabetic column (like in Excel)
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
    self.COLUMNS = columns
    return

  # Use the gridseed in settings to randomize the order of the wordlist.
  # Using a gridseed means that randomization is deterministic (i.e. can be replicated)
  def randomizeWordList(self):
    GRIDSEED = self.config['SETTINGS']['gridseed']
    WORDLIST = self.IMPORTED_WORDLIST
    random.seed(GRIDSEED)
    random.seed(random.getrandbits(128))
    random.shuffle(WORDLIST)
    self.RANDOMIZED_WORDLIST = WORDLIST
    return

  # Apply the order of the wordlist to the columns we created
  # Order is left to right, top to bottom (e.g. A1, B1, C1, A2, B2, C2, etc.)
  def populateGrid(self):
    CELLS = int(self.config['SETTINGS']['gridcols']) * int(self.config['SETTINGS']['gridrows'])
    WORDLIST = self.IMPORTED_WORDLIST
    COLUMNS = self.COLUMNS
    GRIDCOLS = int(self.config['SETTINGS']['gridcols'])

    currentWord = 0
    currentColumn = 1
    currentRow = 1
    GRID = {}

    while currentWord in range(0,CELLS):
      if currentRow <= int(self.config['SETTINGS']['gridrows']):
        if (currentWord + 1) in range(0,len(WORDLIST)):
            currentCell = COLUMNS[currentColumn - 1] + str(currentRow).zfill(2)
            GRID[currentCell] = WORDLIST[currentWord]
            if currentColumn // GRIDCOLS == 0:
              currentColumn += 1
            else:
              currentColumn = 1
              currentRow += 1
            currentWord += 1
        else:
          break
    self.GRID = GRID
    return

  def makeFinal(self):
    with open(self.config['SETTINGS']['gridjson'], 'w') as f:
      json.dump(self.GRID, f)
    print('done!')

def main():
  config = padConfig.Config()
  config.init_config()
  wordlist = WordList(config)
  wordlist.generate_wordlist()
  wordlist.makeFinal()

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    try:
      exit()
    except SystemExit:
      exit()