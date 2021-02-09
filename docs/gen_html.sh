#!/bin/sh

pandoc index.md -o index.html
pandoc til.md -o til.html
pandoc sobtr.md -o sobtr.html
python3 add_viewport.py
