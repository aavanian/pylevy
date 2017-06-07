#!/usr/bin/env python

from distutils.core import setup
import levy

setup(name='PyLevy',
      version=levy.__version__,
      author='Paul Harrison',
      author_email='pfh@logarithmic.net',
      url='http://www.logarithmic.net/pfh/pylevy',
      license='GPL',
      description='A package for calculating and fitting Levy stable distributions.',
      long_description=levy.__doc__,
      py_modules=['levy', 'levy_data', 'levy_approx_data'],
      options={'sdist': {'force_manifest': True}}
      )


# todo - a bunch of things:
#     - remove useless code -> one branch, after all the rest done
#     - discuss moving from writing .py files to writing to a serialized format and load this. Possible issues: backward compability if using new libs and
#       introducing dependencies (could fall back on pickle if preferred format not available
#     - modernize or futurize?
#     - tox and Travis-CI
#     - tests
#     - conform to scipy api for distributions
#     - conda package