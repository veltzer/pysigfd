#!/bin/sh
# via setuptools
#python3 setup.py sdist upload -r pypi --identity="Mark Veltzer" --sign
# via twine
python3 setup.py sdist --identity="Mark Veltzer" --sign
twine upload dist/*
