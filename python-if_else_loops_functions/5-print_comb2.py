#!/usr/bin/python3
for number in range(00, 100):
    if number not in [99]:
        print("{:02d}".format(number), end=", ")
    else:
        print("{}".format(number))
