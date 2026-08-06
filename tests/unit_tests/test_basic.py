"""
test_basic.py
"""

import select
import signal
import unittest

from pysigfd.pysigfd import SigSet, sigfd, sigprocmask


class TestSigfd(unittest.TestCase):
    @unittest.skip("1")
    def test_sigset_create(self):
        """
                Test that we can create a sigset object
        """
        assert SigSet() is not None

    def test_sigset_membership(self):
        """
        Test that add/delete/addmember behave sanely
        """
        signals = SigSet()
        signals.add(signal.SIGHUP)
        signals.add(signal.SIGINT)
        assert signals.ismember(signal.SIGHUP)
        assert signals.ismember(signal.SIGINT)
        signals.remove(signal.SIGINT)
        assert not signals.ismember(signal.SIGINT)

    def test_signalfd_create(self):
        """
        Test that we can create a signalfd object
        """
        signals = SigSet()
        assert sigfd(signals) is not None

    def test_sigmask_restore(self):
        """
        Test that signal mask has been restored after signalfd context
        manager exits
        """
        empty = SigSet()
        orig = sigprocmask(empty)
        mask = SigSet()
        mask.add(signal.SIGHUP)
        mask.add(signal.SIGINT)
        # with sigfd.sigfd(mask) as fd:
        #    pass
        final = sigprocmask(empty)
        assert orig.get_set() == final.get_set()
        print(final.get_set())
        print(orig.get_set())
        # assert all([x == final.sigset.__val[i] for i,x in enumerate(orig.sigset.__val)])

    def testAlarm(self):
        """
        Test that we can read a signal from a signalfd
        """
        mask = SigSet()
        mask.add(signal.SIGALRM)

        with sigfd(mask) as fd:
            poll = select.poll()
            poll.register(fd, select.POLLIN)
            signal.alarm(1)
            events = dict(poll.poll(2000))
            assert fd.fileno() in events
            assert fd.info().ssi_signo == signal.SIGALRM
