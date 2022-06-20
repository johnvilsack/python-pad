MENU
1. Build Your Grid
2. Get Some Random Values
3. Build Some Pass Phrases
4. Do it all for me

Nested Menu
  1. Create New Grid
     1. Use Custom Word File
     2. Use Default Word File
  2. Use Existing Grid
     1. Load a File
     2. Use Current (if diff than default) 


# Design Goals
## Grid Builder
   1. Use either an existing list of words or a custom imported csv
   2. Ask how many columns they want the list to be
   3. Generate a grid based on the list and the column
   4. Print Grid# and Word# 

## Random Picker
   1. Input Grid# and Word# or load a grid
   2. How many codes you want to display
   3. Seed value
   4. Display random values on screen

## Phrase Builder
   1. Load a grid
   2. Type values
   3. Print values and hash values

## Backend
1. Code should be easily replicatable in all cases
2. Save settings in ini (configparser)
3. Add seeding to grid generator to further create deterministic steps to recreate data
   

Current
**pad.py** - Generates cartesian values. Option to input how many you want, and seed value used to generate hits.

This is used to generate some random values someone can use to create passphrases on the grid

**zpad.py** - Same as above, but only for Z coordinates

**makeGrid** - Broken

**importjson.py** - Revised builder. It'll create the grid based on the json input. Allows for more XY coordinates

**dictCommonWords.csv** - Big list

**dictCommonCompounds.csv** - My list.

**build.py** - main script
- EXAMPLE: python build.py A01 B01
- 1->16 instantiate $code var
  - Check cli args
    - If found, convert to list
    - else input for code:
  - **main**
    - INPUT uses $code and runs PrepInput
      - PrepInput concantenantes codes and removes whitespace
    - PAD loads hardlinked file at top and runs loadPad
      - Opens the file
    - OUTPUT joins INPUT and PAD to convertCode
    - PHRASE runs joinCode to combine the words
    - PHRASE runs makeHash to create
      - sha256 hash
      - sha512 hash
      - sha512 hash that then passes through sha512 again
    - Results print on screen in JSON
     