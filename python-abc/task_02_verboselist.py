#!/usr/bin/python3
from typing import SupportsIndex
class VerboseList(list):

    def append(self, item):
        super().append(item)
        print("Added {} to the list.".format(item))

    def extend(self, x):
        super().extend(x)
        print("Extended the list with {} items.".format(x))

    def remove(self, item):
        print("Removed {} from the list.".format(item))
        super().remove(item)

    def pop(self, index: SupportsIndex = -1):
        print("Popped {} from the list.".format(index))
        super().pop(index)