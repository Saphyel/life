#!/usr/bin/env python

from setuptools import setup, find_packages
import life

setup(
    name=life.__name__,
    version=life.__version__,
    description='Game of life',
    author=life.__author__,
    author_email=life.__email__,
    url=life.__url__,
    license='MIT',
    platforms='unix',
    classifiers=[
        "Programming Language :: Python :: 2.7",
    ],
    python_requires='>=2.7, <3',
    tests_require=['behave', 'pytest'],
    packages=find_packages('life'),
    zip_safe=False
)

