"""
This is an example of using the git based signalfd module

The URL for this example:
https://github.com/larsks/python-signalfd/raw/master/example.py

References:
http://blog.oddbit.com/2013/11/28/a-python-interface-to-signalfd/
https://github.com/larsks/python-signalfd/tree/master/signalfd
git@github.com:larsks/python-signalfd.git
"""

import os
import select
import sys

import pysigfd

# create a signal set containing all signals.
from pysigfd.pysigfd import SigSet

mask = SigSet()
mask.fill()

with pysigfd.pysigfd.sigfd(mask) as fd:
    poll = select.poll()
    poll.register(fd, select.POLLIN)
    poll.register(sys.stdin, select.POLLIN)

    # Print signals as they are received until user presses <RETURN>.

    print("=" * 70)
    print(f"Send signals to this process ({os.getpid()}) or press RETURN to exit.")
    print("=" * 70)

    while True:
        events = dict(poll.poll())
        if fd.fileno() in events:
            info = fd.info()
            print(f"received signal {info.ssi_signo}")
        if sys.stdin.fileno() in events:
            print("all done")
            break
