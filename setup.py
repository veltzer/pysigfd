import setuptools

setuptools.setup(
    name='pysigfd',
    version='1.3.3',
    description='pysigfd is a module to help you deal with signals within python using the linux signal file \
    description construct',
    long_description='pysigfd is a module to help you deal with signals within python using the linux signal file description construct',
    url='https://github.com/veltzer/pysigfd',
    download_url='https://github.com/veltzer/pysigfd',
    author='Mark Veltzer',
    author_email='mark.veltzer@gmail.com',
    maintainer='Mark Veltzer',
    maintainer_email='mark.veltzer@gmail.com',
    license='MIT',
    platforms=['python3'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
    keywords='signalfd python3 linux',
    packages=setuptools.find_packages(),
    install_requires=[
        'cffi',
    ],
)
