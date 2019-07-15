"""
********************************************************************************
* Name: setup.py
* Author: Nathan Swain
* Created On: 2014
* Copyright: (c) Brigham Young University 2014
* License: BSD 2-Clause
********************************************************************************
"""
import os
from pathlib import Path
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# mangle settings.py if it exists to prevent from being included in installation
settings = Path('tethys_portal/settings.py')
temp_settings = Path('tethys_portal/__settings.tmp')
if settings.is_file():
    settings.rename(temp_settings)

requires = []

version = '3.0.0a2'

setup(
    name='tethys_platform',
    version=version,
    packages=find_packages(exclude=['tethys_tests', 'tethys_tests.*']),
    include_package_data=True,
    license='BSD 2-Clause License',
    description='Primary Tethys Platform Django Site Project',
    long_description=README,
    url='http://tethysplatform.org/',
    author='Nathan Swain',
    author_email='nswain@aquaveo.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    entry_points={
        'console_scripts': ['tethys=tethys_cli:tethys_command', ],
    },
    install_requires=requires,
    extras_require={
        'tests': [
            'requests_mock',
        ],
    },
)

# restore mangled settings.py
if temp_settings.is_file():
    temp_settings.rename(settings)
