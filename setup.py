#!/usr/bin/env python

from setuptools import setup

from data_analysis import __version__

setup(name='data_analysis',
      version=__version__,
      author='Sconzo',
      author_email='sooshie@gmail.com',
      description='Fork of Click Modules for Data Hacking project',
      long_description=open('README.md').read(),
      install_requires=[ 'networkx','pygraphviz','pandas','matplotlib','numpy','patsy','statsmodels'],
      url='https://github.com/sooshie/data_analysis',
      packages=['data_analysis', 'data_analysis.min_hash','data_analysis.lsh_sims',
                'data_analysis.hcluster','data_analysis.simple_stats'],
      classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: BSD License",
      ]
     )
