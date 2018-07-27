#!/usr/bin/env python

#
# Copyright 2017 Brandon Schlueter
# This file is part of ghh.
#
# Ghh is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import os
from setuptools import setup


scripts = [os.path.join('bin', f)
           for f in os.listdir('bin')
           if os.path.isfile(os.path.join('bin', f))]

setup(
    name='ghh',
    description='GitHub Hook Handler',
    author_email='b@schlueter.blue',
    url='http://ghh.schlueter.blue',
    license='GNU General Public License v3 or later (GPLv3+)',
    packages=['ghh'],
    author='Brandon Schlueter',
    version='0.0.1',
    scripts=scripts,
    install_requires=[
        'bjoern',
        'pyyaml',
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Utilities',
    ])
