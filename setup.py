#!/usr/bin/env python

"""b64img package installer.

"""

import sys
from setuptools import setup

exec(open('b64img/__init__.py').read())
setup(name='b64img',
      packages=['b64img'],
      version=__version__,
      description='Base64 Image Handler for Data URIs',
      setup_requires=['setuptools-markdown'],
      install_requires=['pillow'],
      long_description_markdown_filename='README.md',
      author='Lily Seabreeze',
      author_email='lillian.gardenia.seabreeze@gmail.com',
      license='MIT',
      classifiers=['Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'Natural Language :: English',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.5',
                  ],
    )

