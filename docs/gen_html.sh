#!/bin/sh

pandoc index.md -o index.html
pandoc wil.md -o wil.html
pandoc sobtr.md -o sobtr.html
python3 add_viewport.py
