#open file : 'a' = ammend, 'r' = read, 'w' = write, 'r+' = special read+write mode.
file = open('data/data.txt', 'a')

file.write('This is a line with no line break. ')
file.write('This is another line with no line break. ')
file.write('this is even MORE MORE lines of data, but with a linebreak at the end.  \n')

file.close()