# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 20:35:37 2022

@author: ljd3frf
"""

from setuptools import setup, find_packages

setup(
    name='MonteCarlo',
    version='1.0.0',
    url='https://github.com/MonteCarlo.git',
    author='Levi Davis',
    author_email='ljd3frf@virginia.com',
    description='montecarlo simulation module',
    packages=find_packages('numpy', 'pandas','unittest')
)