import signalfd.common # for ffi, crt
import signalfd.constants # for

signalfd.common.ffi.cdef('''
typedef struct {
	unsigned long int __val[%d];
	} sigset_t;
''' % (1024/(8 * signalfd.common.ffi.sizeof('unsigned long int'))))

signalfd.common.ffi.cdef('''
int sigemptyset(sigset_t *set);
int sigfillset(sigset_t *set);
int sigaddset(sigset_t *set, int signum);
int sigdelset(sigset_t *set, int signum);
int sigismember(const sigset_t *set, int signum);
int sigprocmask(int how, const sigset_t *set, sigset_t *oldset);
''')

'''This is a thin wrapper over sigsetops(3)'''
class sigset(object):
	def __init__ (self, signals=None):
		self.sigset = signalfd.common.ffi.new('sigset_t *')
		self.empty()
		if signals is not None:
			self.sigset = signals

	'''Initialize the signal set to empty'''
	def empty(self):
		signalfd.common.crt.sigemptyset(self.sigset)

	'''Initialize the signal set to full, including all signals'''
	def fill(self):
		signalfd.common.crt.sigfillset(self.sigset)

	'''Add the specified signal to the signal set'''
	def add(self, sig):
		signalfd.common.crt.sigaddset(self.sigset, sig)

	'''Remove the specified signal from the signal set'''
	def remove(self, sig):
		signalfd.common.crt.sigdelset(self.sigset, sig)

	'''Test if the specified signal is a member of the signal set'''
	def ismember(self, sig):
		return signalfd.common.crt.sigismember(self.sigset, sig) == 1

'''
Examine and change blocked signals

- `signals` is a sigset object.
- `mode` controls how sigprocmask() interprets the signal mask (see
below)

sigprocmask() is used to fetch and/or change the signal mask of the calling thread.
The signal mask is the set of signals whose delivery is currently blocked for the
caller (see also signal(7) for more details).

The behavior of the call is dependent on the value of mode, as follows.

signalfd.SIG_BLOCK
	The set of blocked signals is the union of the current set and the set
	argument.

signalfd.SIG_UNBLOCK
	The signals in set are removed from the current set of blocked signals. It
	is permissible to attempt to unblock a signal which is not blocked.

signalfd.SIG_SETMASK
	The set of blocked signals is set to the argument set.

'''
def sigprocmask(signals, mode=signalfd.constants.SIG_SETMASK):
	if not mode in [signalfd.constants.SIG_BLOCK, signalfd.constants.SIG_UNBLOCK, signalfd.constants.SIG_SETMASK]:
		raise ValueError('invalid mode')
	oldsignals = signalfd.common.ffi.new('sigset_t *')
	res = signalfd.common.crt.sigprocmask(mode, signals.sigset, oldsignals)
	if res == -1:
		raise OSError()
	return sigset(oldsignals)
