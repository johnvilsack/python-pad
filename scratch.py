# Using the standard library, print 'hello' to the console in blue text
import sys
sys.stdout.write('\x1b[34m')
print('hello')
sys.stdout.write('\x1b[0m')

# Cancel last color used in sys.stdout.write()