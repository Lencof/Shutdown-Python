# __Author__ __Lencof__
# Shutdown Modified №3.py
# A new Shutdown is created this code turns off the computer and after shutdown creates a file with a note on the desktop

import os
os.system('shutdown -s -t 0') 

README = '''
Shutdown done
'''

# Open for 'w'riting
f = open('README.txt', 'w')
# Write text to file
f.write(README)
f.close()

# If no mode is specified
# 'r'ead mode is assumed by default
f = open('README.txt')
while True: # use True
  line = f.readline()
  # Zero length indicates EOF
  if len(line) == 0:
    break
  # The 'line' already has a newline
  # at the end of each line
  # ssince it is reading from a file.
  print(line, end='')
f.close() 
