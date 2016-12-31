import setuptools
import pypandoc

setuptools.setup(
    name = 'pysigfd',
    version = '1.3.0',
    description = 'pysigfd is a module to help you deal with signals within python using the linux signal file description construct',
    long_descriptioni = pypandoc.convert(('README.md', 'rst'),
    url = 'https://github.com/veltzer/pysigfd', 
    author =i 'Mark Veltzer',
    author_email = 'mark.veltzer@gmail.com',
    license = 'PSF',
    classifiers = [
    ],
    keywords = 'signalfd python3 linux',
    package_dir = {'': 'src'},
    packages = setuptools.find_packages('src'),
    install_requires = [
        'cffi',
    ],
)
