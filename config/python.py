""" python depedencies for this project """
from typing import List


dev_requires: List[str] = [
    "pypitools",
]
config_requires: List[str] = [
    "pyclassifiers",
]
install_requires: List[str] = [
    "cffi",
]
build_requires: List[str] = [
    "pymakehelper",
    "pydmt",
    "types-cffi",
]
test_requires: List[str] = [
    "pylint",
    "pytest",
    "pytest-cov",
    "pyflakes",
    "flake8",
    "mypy",
]
requires = config_requires + install_requires + build_requires + test_requires
