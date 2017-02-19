#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='aj-rest-client',
    version='0.1.14',
    author='AJ Bowen',
    license='MIT',
    author_email='aj@soulshake.net',
    packages=find_packages(),
    description='REST API client',
    long_description=open('README.rst').read(),
    url='https://github.com/soulshake/aj-rc',
    keywords='rest api client',
    install_requires=['click==6.0',
                      'arrow==0.5.4',
                      'requests==2.7.0',
                      'tabulate==0.7.5'],
    entry_points="""\
[console_scripts]
rc = rc.__main__:main
""",
    )

