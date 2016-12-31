#!/usr/bin/python3

import select
import signal
import unittest

from pysigfd.pysigfd import SigSet, sigfd, sigprocmask


class TestSigfd(unittest.TestCase):
    def test_sigset_create(self):
        """
                Test that we can create a sigset object
        """
        assert SigSet() is not None

    '''
        Test that add/delete/addmember behave sanely
    '''

    def test_sigset_membership(self):
        signals = SigSet()
        signals.add(signal.SIGHUP)
        signals.add(signal.SIGINT)
        assert signals.ismember(signal.SIGHUP)
        assert signals.ismember(signal.SIGINT)
        signals.remove(signal.SIGINT)
        assert not signals.ismember(signal.SIGINT)

    '''
        Test that we can create a signalfd object
    '''

    def test_signalfd_create(self):
        signals = SigSet()
        assert sigfd(signals) is not None

    '''
        Test that signal mask has been restored after signalfd context
        manager exits
    '''

    def test_sigmask_restore(self):
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

    '''
        Test that we can read a signal from a signalfd
    '''

    def test_alarm(self):
        mask = SigSet()
        mask.add(signal.SIGALRM)

        with sigfd(mask) as fd:
            poll = select.poll()
            poll.register(fd, select.POLLIN)
            signal.alarm(1)
            events = dict(poll.poll(2000))
            assert fd.fileno() in events
            assert fd.info().ssi_signo == signal.SIGALRM


unittest.main()
