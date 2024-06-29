#!/bin/bash

git add .
git commit -m 'Fix: Correct calculation for best combination of resistors

- Fixed the current calculation to properly account for the total resistance.
- Adjusted the voltage drop calculation to correctly determine the voltage across the component.
- Ensured the resulting voltage matches the desired component voltage.
- Verified functionality with example values, producing the correct resistor combination and voltage output.
'
git push -u origin main
git tag v1.3.1
git push --tag
make clean
make upload