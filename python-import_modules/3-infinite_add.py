#!/usr/bin/python3
import sys
sum = 0

for count in range(1, len(sys.argv)):
    sum += int(sys.argv[count])
print(sum)
