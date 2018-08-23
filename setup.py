# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Yet another GeoJSON Parser for Python',
    long_description=readme,
    author='Jürgen Fredriksson',
    author_email='contact@messfuchs.at',
    url='https://github.com/messfuchs-com/geojson-parser',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

