# Copyright 2014 Cisco Systems
#
# (INSERT LICENSING HERE)

from setuptools import setup, find_packages
from distutils.command.install import install as _install

import sys
import platform

if not sys.version_info[0] == 2:
    print "Sorry, Python 3 is not supported (yet)"
    exit()

if sys.version_info[0] == 2 and sys.version_info[1] < 6:
    print "Sorry, Python < 2.6 is not supported"
    exit()

setup(name='ucstools',
      version='1.0',
      description="Python library for simplifying interaction with Cisco UCS",
      author="Matt Oswalt",
      author_email="(fill in Cisco authors here), matt@keepingitclassless.net",
      url="https://github.com/mierdin/ucstools",
      packages=find_packages('.'),
      install_requires=[
                    "setuptools>0.6"
                    ],
      license="(fill in license here)",
      platforms=["Linux; OS X; Windows"],
      keywords=('Cisco', 'UCS', 'Unified Computing Platform'),
      classifiers=[
          'Programming Language :: Python',
          'Topic :: System :: Networking',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ]
      )







