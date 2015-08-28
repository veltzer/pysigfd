import setuptools # for setup

setuptools.setup(
	install_requires=[
		'cffi',
	],
	version = '1.1',
	name = 'signalfd',
	packages = ['signalfd'],
)
