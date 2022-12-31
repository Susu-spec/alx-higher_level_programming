#!/usr/bin/python3

# chr() converts ASCII value to corresponding ASCII character
for i in range(ord('a'), ord('z')+1):
    if (chr(i) not in ['q', 'e']):
        print(''.join('{}'.format(chr(i))), end='')
