#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return (None)

    ret = list(a_dictionary.keys())[0]
    largest = a_dictionary[ret]
    for k in a_dictionary.keys():
        if a_dictionary[k] > largest:
            largest = a_dictionary[k]
            ret = k
    return (ret)
