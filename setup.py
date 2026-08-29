from setuptools import setup
from os import path
import re

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(this_directory, 'pydanfossair', '__init__.py'), encoding='utf-8') as f:
    init_text = f.read()

match = re.search(r"__version__\s*=\s*['\"]([^'\"]+)['\"]", init_text)
if not match:
    raise RuntimeError("Unable to find __version__ in pydanfossair/__init__.py")

package_version = match.group(1)

setup(name='pydanfossair',
    version=package_version,
    description='Python interface for Danfoss Air HRV systems',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/JonasPed/pydanfoss-air',
    author='Jonas Pedersen',
    author_email='jonas@pedersen.ninja',
    license='Apache 2.0',
    packages=['pydanfossair'])
