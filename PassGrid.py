import itertools, random, json, os
from lib import PassGrid_Config

class PassGrid:
  def __init__(self, config):
    self.config = config.config

    self.IMPORTED_WORDLIST = {}
    self.working_wordlist = {}

    self.generated_columns = {}
    self.working_passgrid = {}
  
    # Set random seed by using the value found in settings
    random.seed(self.config['SETTINGS']['gridseed'])

  # Main generator of object
  def create_passgrid(self):
    complete = False

    # First, open the wordlist specified in config
    file_opened = self.open_wordlist_file()

    if file_opened is True:
      # Randomize this list based on gridseed
      list_ready = self.prepare_wordlist()

      if list_ready is True:
        # Make columns
        columns_ready = self.prepare_columns()

        if columns_ready is True:
          # Create actual Grid
          complete = self.generate_passgrid()

    if complete is True:
      msg = "Grid generated successfully!"  
    else:
      msg = "Grid generation failed!"
    return msg

  # Open wordlist dictated in settings
  def open_wordlist_file(self):
    with open(self.config['SETTINGS']['listsdir'] + self.config['SETTINGS']['wordfile'], 'r') as f:
      # Add to object
      self.IMPORTED_WORDLIST = json.load(f)
    return True

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
    return True

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
    return True

  # Apply the order of the wordlist to the columns we created
  # Order is left to right, top to bottom (e.g. A1, B1, C1, A2, B2, C2, etc.)
  def generate_passgrid(self):

    WORDLIST = self.working_wordlist
    COLUMNS = self.generated_columns

    this_column = 0
    this_row = 1
    result = {}

    i = 0
    # Iterate over wordlist
    for this_word in WORDLIST:
      this_cell = COLUMNS[this_column] + str(this_row).zfill(2)
      result[this_cell] = this_word

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

    self.working_passgrid = result

    return True

  def save_passgrid(self):

    # Check if savesdir path exists, otherwise create it
    if not os.path.exists(self.config['SETTINGS']['savesdir']):
      os.makedirs(self.config['SETTINGS']['savesdir'])

    # Save to file
    with open(self.config['SETTINGS']['savesdir'] + self.config['SETTINGS']['gridjson'], 'w') as f:
      json.dump(self.working_passgrid, f)
    return True

def main():
  # Generate config values
  config = PassGrid_Config.PassGrid_Config()
  config.init_config()

  # PassGrid
  passgrid = PassGrid(config)
  passgrid.create_passgrid()

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    try:
      exit()
    except SystemExit:
      exit()