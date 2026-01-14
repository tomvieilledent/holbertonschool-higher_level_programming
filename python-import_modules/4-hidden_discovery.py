#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":

    name = dir(hidden_4)
    sortedName = sorted(name)
    for nameList in sortedName:
        if nameList.startswith("__"):
            continue
        print(nameList)
