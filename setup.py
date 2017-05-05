import sys
import setuptools

if sys.version_info < (2, 7):
    sys.exit('Sorry, Python < 2.7 is not supported')

if sys.version_info >= (3, 0):
    sys.exit('Sorry, Python 3.x or newer is not supported')

setuptools.setup(
    name='pyteryt',
    version='1.0.0',
    author='Konrad Brodecki',
    description='',
    package_dir={'':'src'},
    packages=setuptools.find_packages('src'),
    entry_points={
        'console_scripts': [
            'pyteryt = pyteryt.core.runner:main',
        ]
    }
)
