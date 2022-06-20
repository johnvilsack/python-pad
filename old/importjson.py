import json
from os.path import exists

#Set how many columns you want
def getInput():
  return int(input("Columns (1-26) [Default: 5] ") or 5)
col = getInput()

while col > 26:
  print("Up to 26 columns allowed")
  col = getInput()

# Convert columns to letters
def numToLetter(col):
  result = list(())
  i = 1
  for i in range(col):
    colNumber = int(i)
    colLetter = chr(colNumber+65)
    i += 1
    result.insert(colNumber, colLetter)
  return result

def createGrid(pad, columns):
  thisColumnNumber = 0
  thisColumnLetter = 0
  thisRowNumber = 0
  thisInstance = 0
  thisSheet = {}
  for value in pad:
    thisColumnLetter = columns[thisColumnNumber]
    zeroRowNumber = str(thisRowNumber).zfill(2)
    if thisInstance % len(columns) == 0:
      print("{0}{1}: {2}".format(thisColumnLetter,zeroRowNumber,pad[thisInstance]))
      thisColumnNumber = 0
      thisRowNumber += 1
    else:
      print("{0}{1}: {2}".format(thisColumnLetter,zeroRowNumber,pad[thisInstance]))
      thisColumnNumber += 1
    thisInstance += 1
  return thisSheet

def main(col):
  columns = numToLetter(col)
  file = open('test.json')
  pad = json.load(file)

  createGrid(pad, columns)

main(col)