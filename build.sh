#!/bin/bash

git add .
git commit -m 'ohmslaw 1.2-rc2'
git push -u origin dev
git tag v1.2-rc2
git push --tag
make clean
make upload