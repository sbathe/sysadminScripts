#!/bin/bash
gawk '{for(i=7;i<=NF;i++){print $i}; printf "\n"}' "$@"
