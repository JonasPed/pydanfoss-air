import pydanfossair
from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='pydanfossair',
    version=pydanfossair.__version__,
    description='Python interface for Danfoss Air HRV systems',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/JonasPed/pydanfoss-air',
    author='Jonas Pedersen',
    author_email='jonas@pedersen.ninja',
    license='Apache 2.0',
    packages=['pydanfossair'])

