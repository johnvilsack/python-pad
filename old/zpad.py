import random
import sys, getopt

LETTERS = ['Z']
NUMBERS = [i for i in range(0,13)]

VALUES = int(input("# to get [25]: ") or 25)
SEED = float(input("# to seed? [65535]: ") or 65535)

def buildPool(VALUES, SEED):
  input("Press enter to continue... ")
  POOL = []

  while len(POOL) in range(VALUES):
    random.shuffle(LETTERS)
    random.shuffle(NUMBERS)
    thisLetter = random.choice(LETTERS)
    thisNumber = str(random.choice(NUMBERS)).zfill(2)
    thisValue =(thisLetter + thisNumber)
    if (random.randrange(1,SEED) == random.randrange(1,SEED)):
      POOL.append(thisValue)
      for i in range(0, len(POOL)):
        print(POOL[i], end=" ")
      else:
        print("", end="\n")
    else:
      for i in range(0, len(POOL)):
        print(POOL[i], end=" ")
      else:
        print(thisValue, end="\n")
buildPool(VALUES, SEED)
