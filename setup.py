from os import path as p
from setuptools import setup

# from fork: https://github.com/gilesbrown/pypicache

with open(p.join(p.dirname(__file__), 'requirements.txt')) as requirements:
    install_requires = [line.strip() for line in requirements]

setup(
    name='pypicache',
    version='0.1',
    description='PyPI caching and proxying server',
    author='Michael Twomey',
    author_email='mick@twomeylee.name',
    url='http://readthedocs.org/projects/pypicache/',
    packages=['pypicache'],
    install_requires=install_requires,
)
