#!/usr/bin/python3

import select # for poll, POLLIN
import signal # for SIGALRM, SIGHUP, SIGINT, alarm
import sigfd # for sigset, sigfd, sigprocmask
import unittest # for main

class TestSigfd(unittest.TestCase):
	'''
		Test that we can create a sigset object
	'''
	def test_sigset_create(self):
		assert sigfd.sigset() is not None

	'''
		Test that add/delete/addmember behave sanely
	'''
	def test_sigset_membership(self):
		signals = sigfd.sigset()
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
		signals = sigfd.sigset()
		assert sigfd.sigfd(signals) is not None

	'''
		Test that signal mask has been restored after signalfd context
		manager exits
	'''
	def test_sigmask_restore(self):
		empty = sigfd.sigset()
		orig = sigfd.sigprocmask(empty)
		mask = sigfd.sigset()
		mask.add(signal.SIGHUP)
		mask.add(signal.SIGINT)
		with sigfd.sigfd(mask) as fd:
			pass
		final = sigfd.sigprocmask(empty)
		assert orig.get_set() == final.get_set()
		print(final.get_set())
		print(orig.get_set())
		#assert all([x == final.sigset.__val[i] for i,x in enumerate(orig.sigset.__val)])

	'''
		Test that we can read a signal from a signalfd
	'''
	def test_alarm(self):
		mask = sigfd.sigset()
		mask.add(signal.SIGALRM)

		with sigfd.sigfd(mask) as fd:
			poll=select.poll()
			poll.register(fd, select.POLLIN)
			signal.alarm(1)
			events = dict(poll.poll(2000))
			assert fd.fileno() in events
			assert fd.info().ssi_signo == signal.SIGALRM

unittest.main()
