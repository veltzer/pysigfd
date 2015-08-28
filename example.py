#!/usr/bin/python3

'''
This is an example of using the git based signalfd module

The URL for this example:
https://github.com/larsks/python-signalfd/raw/master/example.py

References:
http://blog.oddbit.com/2013/11/28/a-python-interface-to-signalfd/
https://github.com/larsks/python-signalfd/tree/master/signalfd
git@github.com:larsks/python-signalfd.git
'''

import os # for getpid
import sys # for stdin
import select # for poll, POLLIN
import signalfd.signalfd # for sigfd
import signalfd.sigset # for sigset
import time # for sleep

# create a signal set containing all signals.
mask = signalfd.sigset.sigset()
mask.fill()

with signalfd.signalfd.sigfd(mask) as fd:
	print(fd.fileno())
time.sleep(3600)
poll = select.poll()
poll.register(fd, select.POLLIN)
poll.register(sys.stdin, select.POLLIN)

# Print signals as they are received until user presses <RETURN>.

print('=' * 70)
print('Send signals to this process (%d) or press RETURN to exit.' % os.getpid())
print('=' * 70)

while True:
	events = dict(poll.poll())
	if fd.fileno() in events:
		info = fd.info()
		print('received signal %d' % info.ssi_signo)
	if sys.stdin.fileno() in events:
		print('all done')
		break
