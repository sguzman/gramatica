#!/bin/bash

watchexec --exts py 'clear && date && pycodestyle --verbose --show-pep8 --show-source main.py && python -m compileall main.py && python __pycache__/main.cpython-38.pyc ./moby-dick.txt'
