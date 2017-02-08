#open file : 'a' = ammend, 'r' = read, 'w' = write, 'r+' = special read+write mode.

#goal of this practice app:
#   open file and see how many current lines there are.
#   ask user if we want to write more.
#       if yes, how many more lines?
#   always have the option of cancelling.


import time
import random
import sys

def write_random_numbers(num_of_items):

    print 'opening file... '
    time.sleep(1)
    with open('data/data.txt', 'a') as file:

        for item in range(0, num_of_items):

            randNum = random.randint(0, 100)

            file.write(str(randNum) + '\n')
            print 'writing ' + str(randNum)
            time.sleep(0.01)
        print 'closing file after "with" loop.'


# MAIN LOOP
def main():
    # Check file for data
    num_lines = sum(1 for line in open('data/data.txt'))
    print 'File currently has ' + str(num_lines) + ' lines of data. '

    # prompt user input
    answer1 = raw_input('Do you want to add more? (y/n) ')

    # if user inputs 'no', quit
    if answer1 == 'n' or answer1 == 'N':
        print 'Thanks for playing! '
        sys.exit(0)

    # if user inputs 'yes' proceed.
    elif answer1 == 'y' or answer1 == 'Y':

        # ask user how many lines to add
        answer2 = raw_input('How many lines to add? ')
        print 'Writing ' + answer2 + ' lines to the file.'

        # execute function to add lines
        write_random_numbers(int(answer2))
        print 'Done writing. Thanks for playing!'

    # if input sucks, tell the user they suck.
    else:
        print 'Your answer is somehow wrong. Goodbye.'

# Check to see if it's an imported module, if not, run the main function.
if __name__ == '__main__':
    main()
