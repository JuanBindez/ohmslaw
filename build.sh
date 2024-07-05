#!/bin/bash

git add .
git commit -m 'ohmslaw 2.1.1'
git push -u origin main
git tag v2.1.1
git push --tag
make clean
make upload