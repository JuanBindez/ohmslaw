#!/bin/bash

git add .
git commit -m 'ohmslaw 1.2.0'
git push -u origin main
git tag v1.2.0
git push --tag
make clean
make upload