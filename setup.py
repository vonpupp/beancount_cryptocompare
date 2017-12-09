#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'cryptocompare==0.3'
]

setup_requirements = [
    # TODO(vonpupp): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='beancount_cryptocompare',
    version='0.0.1',
    description="Beancount cryptocompare prices source",
    long_description=readme + '\n\n' + history,
    author="Albert De La Fuente Vigliotti",
    author_email='vonpupp@gmail.com',
    url='https://github.com/vonpupp/beancount_cryptocompare',
    packages=find_packages(include=['beancount_cryptocompare']),
    #packages=[
    #    'beancount_cryptocompare.cryptocompareusd'
    #],
    #entry_points={
    #    'console_scripts': [
    #        'beancount_cryptocompare=sample:main',
    #    ],
    #},
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='beancount_cryptocompare',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
