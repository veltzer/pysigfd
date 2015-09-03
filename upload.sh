#!/bin/sh
# via setuptools
#python3 setup.py sdist upload -r pypi --identity="Mark Veltzer" --sign
# via twine
rm -rf dist
python3 setup.py sdist
twine upload dist/*

# References:
# https://python-packaging-user-guide.readthedocs.org/en/latest/index.html
