#!/bin/bash

git add .
git commit -m 'removed the "find_resistor" and "best_combinations" methods'
git push -u origin dev
git tag v2.0-rc2
git push --tag
make clean
make upload