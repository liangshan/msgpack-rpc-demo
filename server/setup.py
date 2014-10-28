#!/usr/bin/env python
# coding: utf-8

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name = 'msgpack-rpc-python-with-mysql',
    version = '0.1.dev',
    author = 'Liang Shan',
    author_email = '2lisum3@gmail.com',
    description = "MessagePack RPC demo with MySQL example.",
    packages = ['msgpackrpc'],
    install_requires = [
        'msgpack-python == 0.4.2', 
        'tornado >= 3',
        'sqlalchemy == 0.9.8',
        'oursql == 0.9.3.1'
    ]
)
