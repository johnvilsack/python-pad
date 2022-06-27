import json, random
from lib import padConfig

class PhraseMaker:
  def __init__(self, config):
    self.config = config.config
    self.GRID = {}
    self.TESTGRID = {}
  
  def loadGrid(self):
    with open(self.config['SETTINGS']['gridjson'], 'r') as f:
      self.GRID = json.load(f)
    return

  def loadTestGrid(self):
    with open('testgrid.json', 'r') as f:
      self.TESTGRID = json.load(f)
    return


  def get_random_entry(self):
    upper_value = len(self.GRID)-1
    random_index = str(random.randint(0, upper_value))
    for v in self.GRID[random_index]:
      print(self.GRID[random_index]['word'])

  def test(self):
    print(self.TESTGRID)
    randomchoice = random.sample(sorted(self.TESTGRID),1)[0]
    print(randomchoice)


def main():
  config = padConfig.Config()
  config.init_config()
  makepass = PhraseMaker(config)
  makepass.loadGrid()
  makepass.loadTestGrid()
  makepass.test()

#  makepass.get_random_entry()
  # for _ in range(5):
  #   makepass.get_random_entry()

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    try:
      exit()
    except SystemExit:
      exit()