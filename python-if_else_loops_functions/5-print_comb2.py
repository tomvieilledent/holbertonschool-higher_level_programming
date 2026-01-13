#!/usr/bin/python3
for number in range(00, 100):
    if number not in [99]:
        print(f"{number:02d}", end=", ")
    else:
        print(number)
