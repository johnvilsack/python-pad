import sys, itertools

def loadWordFile(file):
  try:
    with open(file) as f:
      DATA = [line.rstrip() for line in f]
      return DATA
  except:
    print("Unable to load file")

def inputWordFile(args):
  if len(args) > 1:
    dictFileName = args[1]
  else:
    dictFileName = input('What is your dictionary file? ')
  return dictFileName

def inputNumberOfColumns():
  columns = input("How many columns do you want?")
  return columns

def createGrid(dict, columns):
  COLVALUES = 'ABC'

  # If using the alphabet only, only use 1 letter to represent columns
  # if columns <= 26:
  #   COLHEADERS = itertools.islice(COLVALUES, 0, columns)
  # else:
  COLHEADERS = itertools.combinations_with_replacement(COLVALUES, 4)
  numIters = COLVALUES % columns
  print(numIters)
  sys.exit()
  for i in COLHEADERS:
    print(i)

  #foo = itertools.combinations_with_replacement(, 2)
  # for i in foo:
  #   print(i)
  # print("done")

##########################################################

def main():
  #dictFileName = inputWordFile(sys.argv)
  #columns = inputNumberOfColumns()
  dictFileName = 'dictCommonWords.csv'
  columns = 2

  # Load your dictionary into DATA
  DATA = loadWordFile(dictFileName)

  print(type(DATA))
  createGrid(DATA, columns)
  print ('foo')









##########################################################
  print("{0} words {1} cols ".format(len(DATA), columns))

if __name__ == "__main__":
  main()

sys.exit()