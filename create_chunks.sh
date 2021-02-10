#!/bin/bash
# Reference: https://stackoverflow.com/questions/1318972/deleting-millions-of-rows-in-mysql

# Expected input format:
: <<!
00669163-4514-4B50-B6E9-50BA232CA5EB
00669DE5-7659-4CD4-A919-6426A2831F35
!

if [ -z "$1" ]
  then
    echo "No chunk size supplied. Invoke: ./sql-chunker.sh 1000 ids.txt"
fi

if [ -z "$2" ]
  then
    echo "No file supplied. Invoke: ./sql-chunker.sh 1000 ids.txt"
fi

function join_by {
    local d=$1
    shift
    echo -n "$1"
    shift
    printf "%s" "${@/#/$d}"
}

while mapfile -t -n "$1" ary && ((${#ary[@]})); do
    printf "DELETE FROM my_cool_table WHERE id IN ('%s');\n" `join_by "','" "${ary[@]}"`
done < "$2"
