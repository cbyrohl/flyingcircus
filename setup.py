#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Setup instructions.

See: https://packaging.python.org/en/latest/distributing.html
"""

# ======================================================================
# :: Future Imports (for Python 2)
from __future__ import (
    division, absolute_import, print_function)
# BUG in setuptools if import unicode_literals

# ======================================================================
# :: Python Standard Library Imports
import os  # Miscellaneous operating system interfaces
import re  # Regular expression operations
from codecs import open  # use a consistent encoding (in Python 2)

# ======================================================================
# :: Choice of the setup tools
from setuptools import setup
from setuptools import find_packages

# ======================================================================
# project specific variables
NAME = 'FlyingCircus'
VERSION_FILEPATH = os.path.join(NAME.lower(), '_version.py')
README_FILEPATH = 'README.rst'

# get the working directory for the setup script
CWD = os.path.realpath(os.path.dirname(__file__))

# get the long description from the README file
with open(os.path.join(CWD, README_FILEPATH), encoding='utf-8') as readme_file:
    LONG_DESCRIPTION_TEXT = readme_file.read()


# ======================================================================
def fix_version(
        version=None,
        source_filepath=VERSION_FILEPATH):
    """
    Fix version in source code.

    Args:
        version (str): version to be used for fixing the source code
        source_filepath (str): Path to file where __version__ is located

    Returns:
        version (str): the actual version text used
    """

    def dummy_version():
        return '0.0.0.0'

    if version is None:
        try:
            from setuptools_scm import get_version
        except ImportError:
            get_version = dummy_version
        version = get_version()

    if not os.path.isfile(source_filepath):
        version_template = \
            '#!/usr/bin/env python3\n' \
            '# -*- coding: utf-8 -*-\n' \
            '"""Package version file."""\n' \
            '# This file is automatically generated by `fix_version()`' \
            ' in the setup script.\n' \
            '__version__ = \'{version}\'\n'.format(version=version)
        with open(source_filepath, 'wb') as io_file:
            io_file.write(version_template.encode('utf-8'))
    else:
        with open(source_filepath, 'rb') as io_file:
            source = io_file.read().decode('utf-8')
            source = re.sub(
                r"__version__ = '.*'",
                "__version__ = '{}'".format(version),
                source, flags=re.UNICODE)
        with open(source_filepath, 'wb') as io_file:
            io_file.write(source.encode('utf-8'))

    return version


# ======================================================================
# :: call the setup tool
setup(
    name=NAME.lower(),

    description='Everything you always wanted to have in Python.*',
    long_description=LONG_DESCRIPTION_TEXT,

    version=fix_version(),

    url='https://bitbucket.org/norok2/' + NAME.lower(),

    author='Riccardo Metere',
    author_email='rick@metere.it',

    license='GPLv3+',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Environment :: Console',
        'Environment :: Other Environment',

        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',

        'License :: OSI Approved :: '
        'GNU General Public License v3 or later (GPLv3+)',

        'Natural Language :: English',

        'Operating System :: POSIX',
        'Operating System :: OS Independent',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',

        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: System',
        'Topic :: Utilities',
    ],

    keywords=['utils', 'misc', 'iterators', 'metaprogramming', 'science',
              'mathematics', 'math', 'physics', 'format', 'formatting',
              'numpy', 'scipy',],

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[
        'setuptools',  # here to ensure proper installation
        'setuptools_scm',  # here to ensure proper installation
        'blessed',
        'numpy',
        'scipy',
        'numexpr',
        'appdirs',
    ],

    setup_requires=[
        'setuptools',
        'setuptools_scm',
    ],

    extras_require={
        # 'blessed': 'blessed',
    },

    package_data={
        # 'flyingcircus': [
        #     'resources/icon.*',
        # ],
    },
    include_package_data=True,

    # data_files=[('share/icons', ['artwork/flyingcircus_logo.svg'])],

    entry_points={
        'console_scripts': [
            # '<exec_name>=<module>.<submodule>:<callable>',
        ],

        'gui_scripts': [
            # '<exec_name>=<module>.<submodule>:<callable>',
        ],
    },
)

# ======================================================================
# :: create user directory
from flyingcircus import pkg_paths
