  # def makeHTML(self):
  #   GRID = self.GRID
  #   GRIDCOLS = int(self.config['SETTINGS']['gridcols'])

  #   printCell = 0
  #   printRow = 0
  #   printCol = 1

  #   f = open('table.html', 'w')
  #   f.write('<html>\n<head>\n')
  #   f.write('\t<style>\n')
  #   f.write('\t\thtml { font-family: monospace; }\n\t\ttable td { font-size: 9pt; border: 1px solid black; padding: 5px; }\n')
  #   f.write('\t</style>\n')
  #   f.write('</head>\n<body>\n')
  #   f.write('<table>\n\t<tr>\n')

  #   for cell in GRID:
  #     cellValue = format(GRID[printCell]['cell'] + ' :: ' + GRID[printCell]['word'])
  #     cellHTML = '\t\t<td>' + cellValue + '</td>\n'
  #     f.write(cellHTML)

  #     if printCol // GRIDCOLS == 0:
  #       printCol += 1
  #     else:
  #       f.write('\t</tr>\n\t<tr>\n')
  #       printCol = 1
  #       printRow += 1
  #     printCell += 1
  #   f.write('\t</tr>\n</table>\n</body>\n</html>')
  #   f.close()
  #   print('Grid Written to HTML')

  