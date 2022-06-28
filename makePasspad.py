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
    NUMBER_OF_COLUMNS = int(self.config['SETTINGS']['gridcols'])
    NUMBER_OF_ROWS = int(self.config['SETTINGS']['gridrows'])
    TOTAL_CELLS = int(self.config['SETTINGS']['gridcols']) * int(self.config['SETTINGS']['gridrows'])


    #this_word = 0
    this_column = 0
    this_row = 1

    result = {}

    # Iterate over wordlist
    for this_word in WORDLIST:
      this_cell = COLUMNS[this_column] + str(this_row).zfill(2)
      result[this_cell] = this_word

      # CHANGE COUNTERS
      # If column iterator isn't above 0:
      if this_column // NUMBER_OF_COLUMNS == 0:
        # Move cursor to next column, same row
        this_column += 1      
      # If end of columns has been reached
      else:
        # Reset Column cursor
        this_column = 1
        # Drop the Row cursor down a line
        this_row += 1 

    self.working_grid = result
    print('{0} {1}'.format(len(result), len(self.working_wordlist)))
    print(result)
    return













  def makeFinal(self):
    with open(self.config['SETTINGS']['gridjson'], 'w') as f:
      json.dump(self.working_grid, f)
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