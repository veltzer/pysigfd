# TOFIX

Findings from a code scan on 2026-10-04.

## High

- `src/pysigfd/pysigfd.py:48` - the comment `/* Kernel timer ID (POSIX timers)` is never closed, so it swallows the next line and the `ssi_band` field disappears from `struct signalfd_siginfo`. Every field after `ssi_tid` is read from the wrong offset (cffi puts `ssi_overrun` at 28 instead of 32), so `info()` returns garbage for `ssi_overrun`, `ssi_status`, `ssi_int`, `ssi_ptr`, `ssi_addr`, etc. Close the comment, and add a test that checks a field past `ssi_tid` (e.g. `ssi_pid == os.getpid()` after `os.kill`).

## Medium

- `src/pysigfd/pysigfd.py:98` - `get_sigs()` and `get_set()` (line 103) only scan `range(32)`, so real-time signals (32..64) in a set are never reported. Iterate `range(1, signal.NSIG)`.
- `tests/unit_tests/test_basic.py:49` - `test_sigmask_restore` has the `with sigfd(mask)` block commented out, so it never enters the context manager and does not test what its docstring says (the mask is restored after `sigfd` exits). Restore the block.
- `tests/unit_tests/test_basic.py:13` - `test_sigset_create` is skipped with the reason `"1"`; un-skip it (it is trivial) or delete it.
- `pyproject.toml:26` - classifier `Operating System :: OS Independent` is wrong: the package calls `signalfd(2)` and is Linux-only. Use `Operating System :: POSIX :: Linux`.

## Low

- `src/pysigfd/pysigfd.py:30` - `uint64_t` is typedef'd as `unsigned long int`, which is 32 bits on 32-bit Linux and breaks the struct layout there; cffi already knows the `<stdint.h>` types, so drop the four hand-written typedefs.
- `src/pysigfd/pysigfd.py:171` - the `info()` docstring promises a list of attributes that never follows, and its example on line 176 is Python 2 (`print "..." % ...`). Fix the docstring.
- `pyproject.toml:75` - `mypy_path = "src:python:scripts"`, but this repo has no `python/` or `scripts/` directory; trim to `src`.
- `rsconstruct.toml:28` - `examples/` is not in the `ruff`/`mypy` `src_dirs` (line 32 too), so `examples/basic.py` is never checked; add it.
- `doc/TODO.txt:1` - empty file; delete it.
