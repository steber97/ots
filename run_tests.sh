#!/bin/bash

if [ $# -ne 2 ]; then
  echo "Usage: $0 <test_directory> <main_py_program>"
  echo "Example: $0 swerc2020/j main.py"
  exit 1
fi

test_dir="$1"
main_py="$2"

for infile in "$test_dir"/*.in; do
  echo "Test case: $(basename "$infile" .in)"

  output=$(python3 "${test_dir}/${main_py}" < "$infile")
  ansfile="${infile%.in}.ans"
  expected=$(cat "$ansfile")
  if [ "$output" != "$expected" ]; then
      echo "    Daaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaang! WRONG ANSWER!"
  else
      echo "    correct!"
  fi
done