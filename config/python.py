""" python deps for this project """

config_requires: list[str] = [
    "pyclassifiers",
]
install_requires: list[str] = [
    "cffi",
]
build_requires: list[str] = [
    "pydmt",
    "pymakehelper",
    # types
    "types-cffi",
]
test_requires: list[str] = [
    "pylint",
    "pytest",
    "mypy",
    "ruff",
]
requires = config_requires + install_requires + build_requires + test_requires
