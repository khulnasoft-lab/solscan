#!/usr/bin/env bash

### Test path filtering across POSIX and Windows

solc-select use 0.8.0
solscan "tests/e2e/config/test_path_filtering/test_path_filtering.sol" --config "tests/e2e/config/test_path_filtering/solscan.config.json" > "output.txt" 2>&1

if ! grep -q "0 result(s) found" "output.txt"
then
  echo "Path filtering across POSIX and Windows failed"
  rm output.txt
  exit 5
else 
  rm output.txt
fi
