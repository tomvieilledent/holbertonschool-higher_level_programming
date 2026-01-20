#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a0 = tuple_a[0] if len(tuple_a) >= 1 else 0
    tuple_b0 = tuple_b[0] if len(tuple_b) >= 1 else 0
    tuple_a1 = tuple_a[1] if len(tuple_a) >= 2 else 0
    tuple_b1 = tuple_b[1] if len(tuple_b) >= 2 else 0
    new_tuple = tuple_a0 + tuple_b0, tuple_a1 + tuple_b1
    return new_tuple