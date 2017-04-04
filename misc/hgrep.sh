#!/bin/bash
if [ -n "$2" ]; then
  grep --color -A2 -ir "$1" "$2"
else
  grep --color -A2 -ir "$@"
fi
