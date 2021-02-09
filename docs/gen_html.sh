#!/bin/sh

pandoc index.md -o index.html
pandoc til.md -o til.html
python3 add_viewport.py
