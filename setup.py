#!/usr/bin/env python
from distutils.core import setup

setup(name='autotrader',
      version='0.1',
      description='A toolkit for backtesting trading strategies, and executing on them',
      author='Andrew van Rooyen',
      packages=['autotrader'],
      entry_points={
          'console_scripts': ['load-data=autotrader.load:main'],
      })
