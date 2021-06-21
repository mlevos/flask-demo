#!/bin/sh

python -m gunicorn -w 1 demo:app -b 0.0.0.0:${PORT}