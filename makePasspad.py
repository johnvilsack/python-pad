import string, itertools, random, json
from lib import padConfig, padTUI, padMenus

class WordList:
  def __init__(self, config):
    self.config = config.config
    self.WORDLIST = {}
    self.COLUMNS = {}
  
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
    self.COLUMNS = columns
    return columns

  def randomizeWordList(self):
    GRIDSEED = self.config['SETTINGS']['gridseed']
    WORDLIST = self.WORDLIST
    random.seed(GRIDSEED)
    random.seed(random.getrandbits(128))
    random.shuffle(WORDLIST)
    return WORDLIST

  def populateGrid(self):
    CELLS = int(self.config['SETTINGS']['gridcols']) * int(self.config['SETTINGS']['gridcols'])
    WORDLIST = self.WORDLIST
    COLUMNS = self.COLUMNS
    GRIDCOLS = int(self.config['SETTINGS']['gridcols'])

    SHEET = {}
    currentWord = 0
    currentColumn = 1
    currentRow = 1
    GRID = {}

    while currentWord in range(0,CELLS):
      if currentRow <= int(self.config['SETTINGS']['gridrows']):
        if (currentWord + 1) in range(0,len(WORDLIST)):
            currentCell = COLUMNS[currentColumn - 1] + str(currentRow).zfill(2)
            GRID[currentWord] = {
              'cell' : currentCell,
              'word' : WORDLIST[currentWord]
            }
            if currentColumn // GRIDCOLS == 0:
              currentColumn += 1
            else:
              currentColumn = 1
              currentRow += 1
            currentWord += 1
        else:
          break
    self.GRID = GRID
    return GRID

  def makeHTML(self):
    GRID = self.GRID
    GRIDCOLS = int(self.config['SETTINGS']['gridcols'])

    printCell = 0
    printRow = 0
    printCol = 1

    f = open('table.html', 'w')
    f.write('<html>\n<head>\n')
    f.write('\t<style>\n')
    f.write('\t\thtml { font-family: monospace; }\n\t\ttable td { font-size: 9pt; border: 1px solid black; padding: 5px; }\n')
    f.write('\t</style>\n')
    f.write('</head>\n<body>\n')
    f.write('<table>\n\t<tr>\n')

    for cell in GRID:
      cellValue = format(GRID[printCell]['cell'] + ' :: ' + GRID[printCell]['word'])
      cellHTML = '\t\t<td>' + cellValue + '</td>\n'
      f.write(cellHTML)

      if printCol // GRIDCOLS == 0:
        printCol += 1
      else:
        f.write('\t</tr>\n\t<tr>\n')
        printCol = 1
        printRow += 1
      printCell += 1
    f.write('\t</tr>\n</table>\n</body>\n</html>')
    f.close()
    print('Grid Written to HTML')

  #def makeFinal(self):
    # f = open('wordlist.json', 'w')
    # f.write(json.dumps(self.WORDLIST))
    # # for value in WORDLIST:
    # #   f.write(value)
    # f.close()

    # f = open('grid.txt', 'w')
    # for value in self.GRID:
    #   f.write(value)
    # f.close()

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
  GRID = wordlist.populateGrid()
  wordlist.makeHTML()

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    try:
      exit()
    except SystemExit:
      exit()