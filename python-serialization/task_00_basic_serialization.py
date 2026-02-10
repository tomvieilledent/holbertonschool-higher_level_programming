#!/usr/bin/python3

import pickle

def serialize_and_save_to_file(data, filename):

    with open(filename, 'w', encoding='utf-8') as file:
        pickle.dump(data, file)   
    pass

def load_and_deserialize(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        pickle.load(file)
    pass