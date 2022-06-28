import string, itertools, random, json
from lib import padConfig

class WordList:
  def __init__(self, config):
    self.config = config.config

    self.IMPORTED_WORDLIST = {}
    self.working_wordlist = {}

    self.generated_columns = {}
    self.working_grid = {}
  
    # Set random seed by using the value found in settings
    random.seed(self.config['SETTINGS']['gridseed'])

  # Main generator of object
  def generate_wordlist(self):
    # First, open the wordlist specified in config
    self.open_wordlist_file()

    # Randomize this list based on gridseed
    self.prepare_wordlist()

    # Make columns
    self.prepare_columns()

    # Create actual Grid
    self.generate_passgrid()   
    return

  # Open wordlist dictated in settings
  # TODO: Maybe change how this works so it loads like settings file
  def open_wordlist_file(self):
    with open(self.config['SETTINGS']['listsdir'] + self.config['SETTINGS']['wordfile'], 'r') as f:
      # Add to object
      self.IMPORTED_WORDLIST = json.load(f)
    return

  # Using a gridseed means that randomization is deterministic (i.e. can be replicated)
  def prepare_wordlist(self):
    # Get the loaded list
    wordlist = self.IMPORTED_WORDLIST
    TOTAL_CELLS = int(self.config['SETTINGS']['gridcols']) * int(self.config['SETTINGS']['gridrows'])

    # When the imported wordlist cannot fill all cells, pull duplicates to populate
    if (len(wordlist) < TOTAL_CELLS):
      # How many additional words we need
      words_to_add = TOTAL_CELLS - len(wordlist)
      # Get those words
      add_to_wordlist = random.choices(wordlist, k=words_to_add)
      # Add to existing list
      wordlist.extend(add_to_wordlist)

    # Shuffle based on the seed
    random.shuffle(wordlist)

    # Populate object with new values matching total number of values needed
    self.working_wordlist = wordlist[0:TOTAL_CELLS]
    return


  # Make Excel-like columns
  def prepare_columns(self):
    NUMBER_OF_COLUMNS = int(self.config['SETTINGS']['gridcols'])
    COLUMN_NAMES = self.config['SETTINGS']['colnames']

    # When you have less columns than values to iterate against, use single char
    if (NUMBER_OF_COLUMNS <= len(COLUMN_NAMES)):
      prod = itertools.product(COLUMN_NAMES)
    # Otherwise, always start with at least 2 values
    else:
      repeatcols = (NUMBER_OF_COLUMNS // len(COLUMN_NAMES)) + 1
      prod = itertools.product(COLUMN_NAMES, repeat=repeatcols)

    result = []
    for values in prod:
      result.append(''.join(values))

    # Populate object with only values needed
    self.generated_columns = result[0:NUMBER_OF_COLUMNS]
    return

  # Apply the order of the wordlist to the columns we created
  # Order is left to right, top to bottom (e.g. A1, B1, C1, A2, B2, C2, etc.)
  def generate_passgrid(self):

    WORDLIST = self.working_wordlist
    COLUMNS = self.generated_columns

    print(COLUMNS)
    print(len(WORDLIST))

    this_column = 0
    this_row = 1
    result = {}

    i = 0

    with open('test.txt', 'w') as f:
      # Iterate over wordlist
      for this_word in WORDLIST:
        this_cell = COLUMNS[this_column] + str(this_row).zfill(2)
        result[this_cell] = this_word
        f.write('{0}: {1}\n'.format(this_cell, this_word))
        #print("[{0} {1}] {2}::{3}".format(this_column, this_row, this_cell, this_word))
        # Compare current column with total columns minus 1 since lists start at 0
        if this_column // (len(COLUMNS)-1) == 0:
          # Increment column
          this_column += 1
        else:
          # Reset column
          this_column = 0
          # Increment row
          this_row += 1
        i += 1
      f.close()
    
    print('{0} words {1} iterations {2} columns {3} rows'.format(len(WORDLIST), i, len(COLUMNS), this_row))
    print('Expected {0} cells'.format(int(self.config['SETTINGS']['gridcols']) * int(self.config['SETTINGS']['gridrows'])))

    self.working_grid = result
    return

  def makeFinal(self):
    with open(self.config['SETTINGS']['gridjson'], 'w') as f:
      json.dump(self.working_grid, f)
    print('done!')

  def makeHTML(self):
    GRID = self.working_grid
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
      cellValue = format(cell + ' :: ' + GRID[cell])
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

def main():
  # Generate config values
  config = padConfig.Config()
  config.init_config()

  # Wordlist
  wordlist = WordList(config)
  wordlist.generate_wordlist()
  wordlist.makeHTML()
  wordlist.makeFinal()

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    try:
      exit()
    except SystemExit:
      exit()