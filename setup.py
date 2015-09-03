import setuptools # for setup
import sys # for version_info, exit
import pypandoc # for convert

if sys.version_info<(3,):
	print('This module is a python 3 module only')
	sys.exit(1)

read_md = lambda f: pypandoc.convert(f, 'rst')

setuptools.setup(
	install_requires=[
		'cffi',
	],
	version = '1.3',
	name = 'sigfd',
	long_description=read_md('README.md'),
	py_modules=['sigfd'],

	# my details
	author='Mark Veltzer',
	author_email = 'mark.veltzer@gmail.com',
	description = 'This is a python signalfd interface module',
	license = 'PSF',
	keywords = 'signalfd python3 linux',
	url = 'https://github.com/veltzer/python-sigfd', 
)
