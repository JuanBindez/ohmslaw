#!/bin/bash

git add .
git commit -m 'removed the "find_resistor" and "best_combinations" methods'
git push -u origin main
git tag v2.0-rc1
git push --tag
make clean
make upload