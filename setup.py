#!/usr/bin/env python

from setuptools import setup, find_packages


setup(name='AdventOfCode2020',
      version='1.0',
      description='AdventOfCode2020',
      author='Sven Sterbling',
      author_email='sven@sterbling.com',
      url='https://github.com/ullumullu/adventofcode2020',
      keywords='coding, sample adventofcode',
      packages=find_packages(),
      python_requires='>=3.9, <4',
      install_requires=[],
      extras_require={
          'tests': [
              'tox',
              'pytest',
              'pytest-cov'
          ],
          'dev': [
              'pylint',
              'pip-tools'
          ]
      }
      )
