#!/bin/sh

pandoc index.md -o index.html
pandoc wil.md -o wil.html
python3 add_viewport.py
