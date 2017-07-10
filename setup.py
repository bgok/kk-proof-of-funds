#!/usr/bin/env python
from setuptools import setup

setup(
    name='kkpof',
    version='0.0.1',
    author='Kenneth Heutmaker (bgok)',
    description='A simple utility that provides a proof of funds for the bitcoins secured by a KeepKey. It finds all /'
                'bitcoin addresses on a KeepKey that have an unspent balance and signs a message with the key /'
                'associated with each of those addresses.',
    url='https://github.com/bgok/kk-proof-of-funds',
    license='MIT',
    scripts=['kkpof'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['keepkey']
)
