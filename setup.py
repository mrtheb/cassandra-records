#!/usr/bin/env python

import os
import sys
from codecs import open

from setuptools import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py register')
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload --universal')
    sys.exit()

requires = ['cassandra-driver', 'tablib', 'docopt']
version = '0.1.0'


def read(f):
    return open(f, encoding='utf-8').read()

setup(
    name='cassandra-records',
    version=version,
    description='SQL for Humans',
    long_description=read('README.rst') + '\n\n' + read('HISTORY.rst'),
    author='Marc Labbe',
    author_email='mrlabbe@gmail.com',
    url='https://github.com/mrtheb/cassandra-records',
    py_modules=['cassandra_records'],
    package_data={'': ['LICENSE']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['cassandra-records=cassandra_records:cli'],
    },
    install_requires=requires,
    license='ISC',
    zip_safe=False,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
    )
)
