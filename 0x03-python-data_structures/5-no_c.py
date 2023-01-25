#!/usr/bin/python3

def no_c(my_string):
    """Remove all characters c and C from a string."""
    new_str = [x for x in my_string if x != 'C' and x != 'c']
    return ("".join(new_str))
