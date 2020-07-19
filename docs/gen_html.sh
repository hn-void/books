#!/bin/sh

pandoc index.md -o index.html
python3 add_viewport.py
