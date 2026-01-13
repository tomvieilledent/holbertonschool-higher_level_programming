#!/usr/bin/python3
for firstDigit in range(0, 10):
    for lastDigit in range(0, 10):
        if firstDigit < lastDigit and firstDigit != lastDigit:
            if firstDigit == 8 and lastDigit == 9:
                print("{}{}".format(firstDigit, lastDigit))
            else:
                print("{}{}".format(firstDigit, lastDigit), end=", ")
