import json, sys, hashlib, os

FILE = 'otp.json'
ANSWER = {}

# Is there a command line argument?
if len(sys.argv) > 1:
  code = ""
  i = 1
  # Condense CLI arguments to make code
  while i < len(sys.argv):
    code = code + sys.argv[i]
    i += 1
else:
# Get user input if no code found at execution
  code = input('Enter code now: ')

def prepInput(code):
  phrase = code.replace(" ", "")
  return [code[i:i+3] for i in range(0, len(code), 3)] 

def loadPad(file):
  file = open(file)
  return json.load(file)

def convertCode(INPUT, PAD):
  result = []
  for value in INPUT:
    try:
      result.append(PAD[value].capitalize())
    except BaseException as err:
      print("{0} of {1} not found. Try again".format(err, INPUT))
  return result

def joinCode(OUTPUT):
  result = ""
  for value in OUTPUT:
    result = result + value
  return result

def makeHash(PHRASE, algo):
  pwd = PHRASE.encode()
  hash = hashlib.new(algo)
  hash.update(pwd)
  return hash.hexdigest()


###################################
def main(code):
  # Get what we input
  INPUT = prepInput(code)

  # Get the passpad file
  PAD = loadPad(FILE)

  # Run the conversion
  OUTPUT = convertCode(INPUT, PAD)
  PHRASE = joinCode(OUTPUT)

  SHA256 = makeHash(PHRASE, 'sha256')
  SHA512 = makeHash(PHRASE, 'sha512')
  SHA2512 = makeHash(SHA512, 'sha512')

  ANSWER['INPUT'] = INPUT
  ANSWER['OUTPUT'] = OUTPUT
  ANSWER['PHRASE'] = PHRASE
  ANSWER['SHA256'] = SHA256
  ANSWER['SHA512'] = SHA512
  ANSWER['SHA2512'] = SHA2512
  
  print(ANSWER)
main(code)
###################################

