#open file : 'a' = ammend, 'r' = read, 'w' = write, 'r+' = special read+write mode.

import time

with open('data/data.txt', 'a') as f:

    print 'file opened for appending.'

    nums = range(1,10)

    for count in nums:
        f.write('Adding more text using the \'with\' keyword. \n')

time.sleep(1)
print 'file closed.'