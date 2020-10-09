#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from setuptools import setup, find_packages
import naos
setup(
    name='naos',
    version=naos.__version__,
    packages=find_packages(),
    author="LavaPower",
    author_email="lavapower84@gmail.com",
    description="A pseudo operating system make in Python with Pygame",
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    include_package_data=True,
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers.
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Planning"
    ],
    entry_points= {
        'console_scripts': [
            'NaOS = naos.naos_app:launch',
        ],
    },
    install_requires=["pygame"]
)