#!/usr/bin/python3

class CountedIterator:

    def __init__(self, value):
        self.__iterator = iter(value)
        self.__x = 0

    def get_count(self):
        return self.__x
    
    def __next__(self):
        next = next(self.__iterator)
        self.__x += 1
        return next