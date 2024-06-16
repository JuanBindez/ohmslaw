#!/bin/bash

git add .
git commit -m 'ohmslaw 1.1.0'
git push -u origin main
git tag v1.1.0
git push --tag
make clean
make upload