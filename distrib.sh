#!/bin/sh

python setup.py sdist
python setup.py sdist upload

rm -rf build dist PKG-INFO
rm -rf base64img.egg-info
