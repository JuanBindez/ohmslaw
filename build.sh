#!/bin/bash

git add .
git commit -m 'docs update'
git push -u origin dev
git tag v1.3-rc1
git push --tag
make clean
make upload