#!/usr/bin/env python

import io
import setuptools

with io.open('README.md', encoding='utf-8') as readme:
    long_description = readme.read()

NAME = 'xrdtools'
DESCRIPTION = 'A collection of tools for XRD data analysis'

setup_params = dict(
    name=NAME,
    version='v0.1.0',
    author="Lukasz Mentel",
    author_email="lmmentel@gmail.com",
    description=DESCRIPTION,
    long_description=long_description,
    url="https://github.com/lmmentel/xrd-to-heatmap",
    py_modules=['xrdtools'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    entry_points={
        'console_scripts': [
            'xrd.py = xrdtools:cli',
        ]
    },
)


if __name__ == '__main__':
    setuptools.setup(**setup_params)
