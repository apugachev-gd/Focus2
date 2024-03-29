#!/usr/bin/env python
# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Focus
# Copyright (C) 2012 Grid Dynamics Consulting Services, Inc
# All Rights Reserved
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program. If not, see
# <http://www.gnu.org/licenses/>.
 

import os
import sys

from setuptools import setup, find_packages


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()

setup(name='focus2',
      version=__import__('focus2').__version__,
      license='GNU LGPL 2.1',
      description='Web UI for Altai Private Cloud for Developers',
      author='GridDynamics Openstack Core Team, (c) GridDynamics',
      author_email='openstack@griddynamics.com',
      url='http://www.griddynamics.com/openstack',

      zip_safe=False,
      platforms='any',

      packages=find_packages(exclude=['tests']),
      include_package_data=True,
      test_suite='tests',
      long_description=read('README.rst'),
      install_requires=[
        'Flask==0.9',
        'Flask-WTF==0.8'],
      tests_require=['mox'],
      classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
        'Operating System :: OS Independent',
       'Programming Language :: Python :: 2.6',
        ]
      )
