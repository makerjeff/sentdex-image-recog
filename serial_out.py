import serial
import time
import sys

def send_serial_slowly(message):
    # strip string to individual string
    # loop through string array
        #write each character out to serial with 0.25s time delay
        #if end of string array
            #send delimter character ';'
    return


print 'opening serial port...'

arduino = serial.Serial('/dev/cu.usbmodem14111', 9600, timeout=1)
time.sleep(2)
print 'initialized.'

prompt1 = raw_input('Do you want to send a message to the serial port? (y/n): ')

if prompt1 == 'n':
    print 'Thanks for playing!  Goodbye.'
    sys.exit(0)
elif prompt1 == 'y':
    prompt2 = raw_input('What would you like to send? ')

    print 'Sending message through serialport...'
    arduino.write(prompt2)

    print ' message sent: ' + prompt2
    print ' Thanks for playing! Goodbye. '
    sys.exit(0)
