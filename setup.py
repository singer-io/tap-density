#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='tap-density',
      version='0.0.1',
      description='Singer.io tap for extracting data from the Density.io API',
      author='sinaenvoy.com',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_density'],
      install_requires=[
        'tap-framework==0.0.5'
      ],
      entry_points='''
          [console_scripts]
          tap-density=tap_density:main
      ''',
      packages=find_packages(),
      package_data={
          'tap_density': [
              'schemas/*.json'
          ]
      })
