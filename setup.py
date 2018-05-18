from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.1'

install_requires = [
    # List your project dependencies here.
    # For more details, see:
    # http://packages.python.org/distribute/setuptools.html#declaring-dependencies
]

tests_require = [
    'pytest>=2.4.0',
    'pytest-mock',
]

setup(
    name='mtginator',
    version=version,
    description="Magic: The Gathering Goldfishing Module",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='',
    author='Benjamin Hitz',
    author_email='hitz@stanford.edu',
    url='http://chumpblock.com',
    license='MIT',
    packages=find_packages('src'),
    package_dir={'': 'src'}, include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
    },
    entry_points={
        'console_scripts':
            ['mtginator=mtginator:main']
    }
)
