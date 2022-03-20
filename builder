#!/bin/bash

rm -rf dist/
rm -rf FlavorTexts.egg-info/
python3 -m build
python3 -m twine upload dist/*