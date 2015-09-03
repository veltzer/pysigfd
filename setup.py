import setuptools # for setup
import sys # for version_info, exit

if sys.version_info<(3,):
	print('This module is a python 3 module only')
	sys.exit(1)

setuptools.setup(
	install_requires=[
		'cffi',
	],
	version = '1.2',
	name = 'sigfd',
	py_modules=['sigfd'],

	# my details
	author='Mark Veltzer',
	author_email = 'mark.veltzer@gmail.com',
	description = 'This is a python signalfd interface module',
	license = 'PSF',
	keywords = 'signalfd python3 linux',
	url = 'https://github.com/veltzer/python-sigfd', 
)
